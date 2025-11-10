#!/usr/bin/env python3
import os
import sys
import shutil
import struct
import zipfile
import subprocess as sp
from pathlib import Path

# Constants
KEYSTORE = "debug.keystore"
KEY_ALIAS = "androiddebugkey"
STORE_PASS = "android"
KEY_PASS = "android"
OUT_DIR = Path("out")
MOD_APK = OUT_DIR / "mod.apk"
SIGNED_APK = OUT_DIR / "mod-signed.apk"

LOCAL_FILE_HEADER_SIG = b'\x50\x4b\x03\x04'
CENTRAL_DIR_HEADER_SIG = b'\x50\x4b\x01\x02'

# Utilities
def log(msg): print(f"[+] {msg}")
def err(msg): print(f"[x] {msg}")
def run(cmd):
    result = sp.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        err(result.stderr.strip())
        raise RuntimeError(result.stderr.strip())
    return result.stdout.strip()

# Keystore & Signing
def ensure_debug_keystore():
    if not os.path.exists(KEYSTORE):
        log("Generating debug.keystore")
        run(f"keytool -genkey -v -keystore {KEYSTORE} -alias {KEY_ALIAS} "
            f"-keyalg RSA -keysize 2048 -validity 10000 "
            f"-storepass {STORE_PASS} -keypass {KEY_PASS} "
            f'-dname "CN=Android Debug,O=Android,C=US"')

def sign_apk(input_apk, output_apk):
    log("Signing APK...")
    ensure_debug_keystore()
    run(f"apksigner sign --ks {KEYSTORE} --ks-pass pass:{STORE_PASS} "
        f"--key-pass pass:{KEY_PASS} --min-sdk-version 21 "
        f"--out {output_apk} {input_apk}")

# Manifest Backup
def backup_manifest(apk, out="AndroidManifest_original.bin"):
    with zipfile.ZipFile(apk, 'r') as zipf:
        data = zipf.read("AndroidManifest.xml")
        with open(out, 'wb') as f:
            f.write(data)

# Helper for reading ZIP headers
def get_filename(data, offset):
    if data[offset:offset+4] == LOCAL_FILE_HEADER_SIG:
        name_len = struct.unpack('<H', data[offset + 26:offset + 28])[0]
        extra_len = struct.unpack('<H', data[offset + 28:offset + 30])[0]
        name = data[offset + 30:offset + 30 + name_len].decode(errors='ignore')
        return name, 30 + name_len + extra_len
    elif data[offset:offset+4] == CENTRAL_DIR_HEADER_SIG:
        name_len = struct.unpack('<H', data[offset + 28:offset + 30])[0]
        extra_len = struct.unpack('<H', data[offset + 30:offset + 32])[0]
        comment_len = struct.unpack('<H', data[offset + 32:offset + 34])[0]
        name = data[offset + 46:offset + 46 + name_len].decode(errors='ignore')
        return name, 46 + name_len + extra_len + comment_len
    return None, 1

def should_protect(filename):
    return filename.startswith('classes') and filename.endswith('.dex')

# Encryption flag patcher
def patch_apk(input_apk: str, output_apk: str = None):
    if output_apk:
        shutil.copyfile(input_apk, output_apk)
        target = output_apk
    else:
        target = input_apk

    with open(target, 'r+b') as f:
        data = bytearray(f.read())
        offset = 0

        while offset < len(data):
            sig = data[offset:offset+4]
            if sig in [LOCAL_FILE_HEADER_SIG, CENTRAL_DIR_HEADER_SIG]:
                filename, skip_len = get_filename(data, offset)
                if filename and should_protect(filename):
                    log(f"Setting encryption flag for: {filename}")
                    flags_offset = offset + 6 if sig == LOCAL_FILE_HEADER_SIG else offset + 8
                    data[flags_offset] |= 0x01
                offset += skip_len
            else:
                offset += 1

        f.seek(0)
        f.write(data)

    log(f"[✓] Protection (encryption flag only) applied to {target}")

# Header tampering
def tamper_lfh_compression_and_flags(apk_path):
    log("Tampering LFH entries: compression method + reserved bit")
    count = 0
    with open(apk_path, 'r+b') as f:
        data = f.read()
        offset = 0
        while offset < len(data) - 30:
            if data[offset:offset+4] == LOCAL_FILE_HEADER_SIG:
                comp_off = offset + 8
                flag_off = offset + 6
                orig_method = struct.unpack_from('<H', data, comp_off)[0]
                if orig_method in (0x08, 0x00):  # deflate or store
                    f.seek(comp_off)
                    f.write(struct.pack('<H', 0x99))  # Invalid compression
                    f.seek(flag_off)
                    orig_flag = struct.unpack_from('<H', data, flag_off)[0]
                    f.write(struct.pack('<H', orig_flag ^ 0x4000))  # Reserved bit
                    count += 1
            offset += 1
    log(f"Tampered {count} LFH entries")

# Full process
def setup(input_apk):
    if not os.path.exists(input_apk):
        err(f"APK not found: {input_apk}")
        sys.exit(1)

    OUT_DIR.mkdir(exist_ok=True)
    log("Copying APK")
    shutil.copy2(input_apk, MOD_APK)

    backup_manifest(MOD_APK)
    patch_apk(MOD_APK)  # Apply encryption flag to .dex files
    tamper_lfh_compression_and_flags(MOD_APK)
    sign_apk(MOD_APK, SIGNED_APK)

    log(f"[✓] Final APK ready: {SIGNED_APK}")

# Entry point
def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <app.apk>")
        sys.exit(1)
    setup(sys.argv[1])

if __name__ == "__main__":
    main()
