import argparse
import os
import subprocess
import shutil
import sys
import tempfile
from pathlib import Path
import json 
import re

# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"

ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

class TeeOutput:
    def __init__(self, terminal_stream, log_stream):
        self.terminal_stream = terminal_stream
        self.log_stream = log_stream

    def write(self, message):
        self.terminal_stream.write(message)
        self.terminal_stream.flush()
        # Strip ANSI before writing to log
        self.log_stream.write(ansi_escape.sub('', message))
        self.log_stream.flush()

    def flush(self):
        self.terminal_stream.flush()
        self.log_stream.flush()


def info(msg): print(f"{CYAN}[INFO]{RESET} {msg}")
def success(msg): print(f"{GREEN}[\u2713]{RESET} {msg}")
def warn(msg): print(f"{YELLOW}[!]{RESET} {msg}")
def error(msg): print(f"{RED}[\u2717]{RESET} {msg}"); sys.exit(1)

def format_size(bytes):
    for unit in ['B', 'KB', 'MB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024
    return f"{bytes:.2f} MB"

def run_cmd(cmd, cwd=None, silent=False):
    info(f"Executing: {cmd}")
    stdout_opt = subprocess.DEVNULL if silent else None
    stderr_opt = subprocess.DEVNULL if silent else None

    result = subprocess.run(cmd, shell=True, cwd=cwd, stdout=stdout_opt, stderr=stderr_opt)
    if result.returncode != 0:
        error(f"Command failed: {cmd}")

def cleanup_temp_dir(temp_dir):
    try:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            success(f"Cleaned up temp directory: {temp_dir}")
    except Exception as e:
        warn(f"Failed to delete temporary directory: {e}")

def run_apktool_decompile(apk_path, out_dir):
    info("Decompiling APK with apktool...")
    apktool_path = os.path.join(os.getcwd(), "apk-packer/tools/apktool.jar")
    if not os.path.exists(apktool_path):
        error("apktool.jar not found in apk-packer/tools/")
    run_cmd(f'java -jar "{apktool_path}" d -f "{apk_path}" -o "{out_dir}"')

def find_smali_files_by_keywords(base_dir, package_path, keywords):
    matched_files = []
    unmatched = []

    target_path = os.path.join(base_dir, "smali")
    for root, _, files in os.walk(target_path):
        if package_path.replace(".", os.sep) not in root:
            continue
        for file in files:
            if file.endswith(".smali"):
                path = os.path.join(root, file)
                filename_lower = file.lower()
                if any(k in filename_lower for k in keywords):
                    matched_files.append(path)
                else:
                    unmatched.append(path)

    return  unmatched

def copy_file(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
    success(f"Smali file updated at: {dst}")

def main():
    

    parser = argparse.ArgumentParser(description="\ud83d\udd27 Auto APK Obfuscation Pipeline")
    parser.add_argument("apk_path", help="Path to the APK file")
    parser.add_argument("package", help="Java-style package name (e.g., com.ujjivan.voice)")
    args = parser.parse_args()
    
    apk_path = os.path.abspath(args.apk_path)
    apk_name = os.path.basename(apk_path)[:-4]
    package = args.package

    log_file = open(os.path.basename(apk_path)[:-4]+"_LOGS.txt", "w", encoding="utf-8")
    sys.stdout = TeeOutput(sys.stdout, log_file)
    sys.stderr = TeeOutput(sys.stderr, log_file)

    smali_with_goto_count = 0
    if not os.path.exists(apk_path):
        error(f"APK not found: {apk_path}")

    temp_dir = tempfile.mkdtemp()
    info(f"Working in temp directory: {temp_dir}")

    run_apktool_decompile(apk_path, temp_dir)

    keywords = ["activity", "fragment", "view", "camera"]
    matched_files = find_smali_files_by_keywords(temp_dir, package, keywords)

    print(f"\n\U0001f5c3 Matched smali files: {len(matched_files)}")
    for path in matched_files:
        print(f"  -> {path}")

    if not matched_files:
        warn("No matching smali files found. Exiting.")
        cleanup_temp_dir(temp_dir)
        return

    total_smali = len(matched_files)
    obfuscated_smali_count = 0
    total_methods_obfuscated = 0
    total_methods_with_goto = 0

    for smali_path in matched_files:
        smali_name = Path(smali_path).name.replace(".smali", "")
        smali_json = smali_name + ".json"

        run_cmd(["python", "Engine.py", smali_path,apk_name], cwd="./CFG")
        run_cmd(["python", "restructure_cfg.py", f"../CFG/json_outputs/{apk_name}/{smali_json}",apk_name], cwd="./CFG_GRAPH_BUILDER")

        # Prepare to collect stats
        stats_temp = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
        stats_env = os.environ.copy()
        stats_env["STATS_FILE"] = stats_temp.name

        # Run obfuscator
        obf_proc = subprocess.run(
            ["python", "obfuscator.py", f"../CFG_GRAPH_BUILDER/restructured_jsons/{apk_name}/{smali_name}_restructured.json",apk_name],
            cwd="./injection",
            env=stats_env
        )

        if obf_proc.returncode == 100:
            warn(f"{RED}No obfuscation (no gotos) in: {smali_name}. Skipping.")
            continue
        elif obf_proc.returncode != 0:
            error(f"Obfuscator failed for: {smali_name}")

        # Now try reading stats
        try:
            with open(stats_temp.name, "r") as f:
                method_stats = json.load(f)

                # Count methods
                obf_methods = sum(1 for m in method_stats.values() if m.get("obfuscated"))
                goto_methods = sum(1 for m in method_stats.values() if m.get("goto_count", 0) > 0)

                total_methods_obfuscated += obf_methods
                total_methods_with_goto += goto_methods

                # Count smali files with at least one goto
                if goto_methods > 0:
                    smali_with_goto_count += 1

        except Exception as e:
            warn(f"Could not read stats for {smali_name}: {e}")

        obfuscated_smali_count += 1

        # Assemble and copy
        run_cmd([
            "python", "assembler.py",
            f"../Injection/obfuscated_jsons/{apk_name}/obfuscated_{smali_name}_restructured.json",
            apk_name,"--injected"
        ], cwd="./assembler")

        output_smali = f"./assembler/assembled_smali/{apk_name}/modified_obfuscated_{smali_name}_restructured.smali"
        copy_file(output_smali, smali_path)



    print(f"\n{CYAN}{'=' * 30} CONTROL FLOW OBFUSCATION SUMMARY {'=' * 30}{RESET}")
    print(f"{YELLOW}🔹 Total smali matched:                  {RESET}{total_smali}")
    print(f"{YELLOW}🔹 Smali files containing 'goto':       {RESET}{smali_with_goto_count}")
    print(f"{YELLOW}🔹 Smali files obfuscated:              {RESET}{GREEN if obfuscated_smali_count else RED}{obfuscated_smali_count}{RESET}")
    print(f"{YELLOW}🔹 Total methods obfuscated:            {RESET}{total_methods_obfuscated}")
    print(f"{YELLOW}🔹 Total methods with 'goto':           {RESET}{total_methods_with_goto}")

    # Smali files with gotos
    smali_with_goto_count = total_methods_with_goto  # you can improve this with file-based stat collection later

    if total_smali:
        coverage = (obfuscated_smali_count / total_smali) * 100
        print(f"{CYAN}✅ Obfuscation coverage (smali):        {RESET}{BOLD}{GREEN if coverage >= 50 else YELLOW}"
            f"{coverage:.2f}%{RESET} {MAGENTA}[{obfuscated_smali_count}/{total_smali}]{RESET}")

    if total_methods_with_goto:
        method_coverage = (total_methods_obfuscated / total_methods_with_goto) * 100
        print(f"{CYAN}✅ Coverage (methods with goto):        {RESET}{BOLD}{GREEN if method_coverage >= 50 else YELLOW}"
            f"{method_coverage:.2f}%{RESET} {MAGENTA}[{total_methods_obfuscated}/{total_methods_with_goto}]{RESET}")

    if smali_with_goto_count:
        smali_goto_coverage = (obfuscated_smali_count / smali_with_goto_count) * 100
        print(f"{CYAN}✅ Smali obfuscation (where goto exists): {RESET}{BOLD}"
            f"{GREEN if smali_goto_coverage >= 50 else YELLOW}{smali_goto_coverage:.2f}%{RESET} "
            f"{MAGENTA}[{obfuscated_smali_count}/{total_smali}]{RESET}")
    print(f"{CYAN}{'=' * 80}{RESET}")




    run_cmd(f"python packer.py {temp_dir}", cwd="./apk-packer", silent=False)
    output_apk = os.path.join(os.getcwd(), f"apk-packer/modified/{os.path.basename(temp_dir)}.apk")

    original_size = os.path.getsize(apk_path)
    info(f"Original APK size: {format_size(original_size)}")

    if os.path.exists(output_apk):
        success(f"Modified APK created at: {output_apk}")
        modified_size = os.path.getsize(output_apk)
        info(f"Modified APK size: {format_size(modified_size)}")

        diff = modified_size - original_size
        if diff > 0:
            print(f"{YELLOW}📈 Size increased by: {format_size(diff)}{RESET}")
        elif diff < 0:
            print(f"{GREEN}📉 Size decreased by: {format_size(abs(diff))}{RESET}")
        else:
            print(f"{MAGENTA}➖ APK size unchanged.{RESET}")
    else:
        error("APK packing failed.")

    cleanup_temp_dir(temp_dir)
    success("All done.")
    log_file.close()

if __name__ == "__main__":
    main()
