import os
import sys
import subprocess
import tempfile
import shutil
import xml.etree.ElementTree as ET



def recompile_apk(temp_dir, output_apk_name="modified_output.apk"):
    print("[+] Recompiling the APK using apktool...\n")
    try:
        java_path = "java"  
        apktool_path = os.path.join(os.getcwd(), "./tools/apktool.jar")
        subprocess.run([java_path, "-jar", apktool_path, "b", temp_dir, "-o", output_apk_name], check=True)
        print(f"[+] APK recompiled successfully: {os.path.abspath(output_apk_name)}")
    except subprocess.CalledProcessError:
        print("[-] Error: Failed to compile the APK using apktool.")
    except FileNotFoundError:
        print("[-] Apktool is not installed or not in PATH.")
    finally:
        print("\n [+] Recompilation Successful.")


def apk_signing(apk_path):
    print(f"[+] Signing APK: {apk_path}")
    if not os.path.exists(apk_path):
        print("[-] APK file does not exist.")
        return

    apk_abs = os.path.abspath(apk_path)
    apk_dir = os.path.dirname(apk_abs)

    # Run uber-apk-signer on the APK
    cmd = [
        "java", "-jar", "./tools/uber-apk-signer-1.3.0.jar",
        "-a", apk_abs,
        "--overwrite"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("[-] APK signing failed:")
        print(result.stderr)
        return

    # Find the signed APK inside 'output' directory
    signed_apk_name = os.path.basename(apk_path).replace(".apk", "-aligned-debugSigned.apk")
    signed_apk_path = os.path.join(apk_dir, "output", signed_apk_name)

    if not os.path.exists(signed_apk_path):
        return

    # Replace original with signed APK
    shutil.move(signed_apk_path, apk_abs)
    print(f"[+] APK signed successfully and replaced: {apk_abs}")

    # Optional cleanup
    shutil.rmtree(os.path.join(apk_dir, "output"), ignore_errors=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python packer.py <path_to_decompiled_apk_folder>")
        sys.exit(1)

    input_dir = sys.argv[1]
    if not os.path.isdir(input_dir):
        print("[-] Given path is not a directory.")
        sys.exit(1)

    base_name = os.path.basename(os.path.normpath(input_dir)) + ".apk"
    output_dir = "./modified"
    os.makedirs(output_dir, exist_ok=True)

    output_apk_path = os.path.join(output_dir, base_name)

    recompile_apk(input_dir, output_apk_path)
    apk_signing(output_apk_path)

