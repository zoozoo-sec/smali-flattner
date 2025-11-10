import sys
import json 
import os

def flatten_restructured_json(cfg):
    if "blocks" in cfg:
        return cfg  # already flattened

    flat_blocks = []
    for key, val in cfg.items():
        if key == "class_directives":
            continue
        if isinstance(val, dict) and "blocks" in val:
            flat_blocks.extend(val["blocks"])

    return {
        "class_directives": cfg.get("class_directives", []),
        "blocks": flat_blocks
    }

def Assembler(cfg,output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        # Step 1: Write class directives
        for directive in cfg.get("class_directives", []):
            f.write(f"{directive}\n")
        f.write("\n")
        # Step 2: Group blocks by method name
        method_blocks = {}
        for block in cfg["blocks"]:
            method = block["method"]
            method_blocks.setdefault(method, []).append(block)

        # Step 3: For each method, sort blocks by ID and reconstruct
        for method, blocks in method_blocks.items():
            blocks.sort(key=lambda b: b["id"])  # optional, to preserve order
            for block in blocks:
                # Entry block
                if block.get("is_entry", False):
                    for directive in block.get("directives", []):
                        f.write(f"{directive}\n")
                    register_info = block.get("register_info", {})
                    if "locals" in register_info:
                        f.write(f".locals {register_info['locals']}\n")
                    if "registers" in register_info:
                        f.write(f".registers {register_info['registers']}\n")
                    params = register_info.get("params", {})
                    for reg, name in params.items():
                        f.write(f".param {reg}, \"{name}\"\n")
                    f.write("\n")

                # Write label if present
                label = block.get("label")
                if isinstance(label, str):
                    f.write(f":{label}\n")
                elif isinstance(label, list):
                    for l in label:
                        f.write(f":{l}\n")

                inside_switch = False
                for instr in block.get("instructions", []):
                    instr = instr.strip()
                    if instr.startswith(".packed-switch") or instr.startswith(".sparse-switch"):
                        inside_switch = True
                        f.write(f"    {instr}\n")
                        continue
                    if instr == ".end packed-switch" or instr == ".end sparse-switch":
                        inside_switch = False
                        f.write(f"    {instr}\n")
                        continue
                    if inside_switch:
                        f.write(f"    {instr}\n")
                        continue

                    f.write(f"    {instr}\n")

                # Exit block
                if block.get("is_exit", False):
                    for directive in block.get("directives", []):
                        f.write(f"{directive}\n")
                    f.write("\n")

    print(f"[+] Successfully reconstructed Smali file: {output_file}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python Assembler.py <cfg_object.json> [--injected]")
        sys.exit(1)

    json_file = sys.argv[1]
    output_subdir = sys.argv[2]
    injected_mode = "--injected" in sys.argv

    try:
        with open(json_file, "r", encoding="utf-8") as f:
            json_obj = json.load(f)
        print("[+] Successfully loaded JSON file!")
    except Exception as e:
        print(f"[-] Failed to load JSON file: {e}")
        sys.exit(1)

    # modify json only if --injected is passed
    if injected_mode:
        print("[+] Flattening restructured JSON...")
        json_obj = flatten_restructured_json(json_obj)

    base_name = os.path.basename(json_file)
    name_without_ext = os.path.splitext(base_name)[0]
    output_dir = os.path.join("assembled_smali", output_subdir)
    os.makedirs(output_dir, exist_ok=True) 
    if injected_mode:
        output_file = os.path.join(output_dir, f"modified_{name_without_ext}.smali")
    else:
        output_file = os.path.join(output_dir, f"{name_without_ext}.smali")

    Assembler(json_obj, output_file)