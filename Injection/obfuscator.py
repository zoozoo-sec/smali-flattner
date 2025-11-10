import json
import os
import re
import sys
import copy
import re
import random

# Terminal color helpers
def green(text): return f"\033[92m{text}\033[0m"
def red(text): return f"\033[91m{text}\033[0m"
def yellow(text): return f"\033[93m{text}\033[0m"
def cyan(text): return f"\033[96m{text}\033[0m"
def bold(text): return f"\033[1m{text}\033[0m"


import random



def count_method_parameters(method_signature):
    """
    Parses the method signature and returns the total number of register slots
    used by parameters, including 'this' for non-static methods.
    E.g., (Ljava/lang/String;ID)V → 1 + 1 (String) + 1 (int) + 2 (double) = 5
    """
    match = re.search(r'\((.*?)\)', method_signature)
    if not match:
        return 0

    param_str = match.group(1)
    count = 1  # p0 = 'this' (assume non-static)

    i = 0
    while i < len(param_str):
        c = param_str[i]
        if c in 'ZBSCIF':  # single-width primitives
            count += 1
            i += 1
        elif c in 'JD':  # wide primitives
            count += 2
            i += 1
        elif c == 'L':  # object reference
            end = param_str.find(';', i)
            if end == -1:
                break
            count += 1
            i = end + 1
        elif c == '[':  # array type
            i += 1
            while i < len(param_str) and param_str[i] == '[':
                i += 1
            if i < len(param_str) and param_str[i] == 'L':
                end = param_str.find(';', i)
                i = end + 1 if end != -1 else len(param_str)
            else:
                i += 1
            count += 1
        else:
            i += 1  # fallback

    return count


def extract_used_registers(blocks):
    """Extract all vN registers used in all instructions of a method."""
    reg_pattern = re.compile(r'\bv(\d+)\b')
    used = set()
    for block in blocks:
        for instr in block.get("instructions", []):
            matches = reg_pattern.findall(instr)
            for m in matches:
                used.add(int(m))
    return used

def choose_register(locals_count, used_regs, max_limit=15):
    """
    Choose a register to use for opaque logic.
    - If locals < max_limit: return next safe register
    - If locals ≥ max_limit: return first unused register from 0–13
    """
    if locals_count <= max_limit:
        return locals_count, True  # Safe to extend

    for i in range(max_limit):
        if i not in used_regs:
            return i, False  # Reuse a safe temporary register

    return 4, False  # Fallback (warning: might overwrite live value)

def extract_method_signature_from_directives(blocks):
    entry_block = next((b for b in blocks if b.get("is_entry")), None)
    if entry_block:
        directive = entry_block.get("directives")[0]
        if directive.strip().startswith(".method"):
            match = re.search(r'\((.*?)\)', directive)
            if match:
                return f"({match.group(1)})"
    return ""


def transform_method_blocks(json_data, method_blocks, method_name, stats):
    blocks = method_blocks["blocks"]
    entry_block = next((b for b in blocks if b.get("is_entry")), None)
    locals_count = int(entry_block["register_info"].get("locals", "0")) if entry_block else 0


    method_signature = extract_method_signature_from_directives(blocks)
    param_count = count_method_parameters(method_signature)
    total_registers_needed = locals_count + param_count
    


    # Count how many gotos this method has
    goto_count = sum(
        1 for block in blocks for instr in block.get("instructions", []) if instr.strip().startswith("goto")
    )

    if method_name=="<init>":
        for block in blocks:
            for instr in block.get("instructions", []):
                if instr.strip().startswith("goto"):
                    print(instr)
        
    
    stats[method_name] = {
        "goto_count": goto_count,
        "obfuscated": goto_count > 0
    }
    if (goto_count == 0 or "synthetic" in method_name):
        return method_blocks  # Nothing to transform

    # Determine which registers are used to avoid clobbering
    used_regs = extract_used_registers(blocks)
    new_reg_index, safe_to_extend = choose_register(locals_count, used_regs)

    # If we cannot inject safely, skip
    if total_registers_needed > 15:
        stats[method_name]["obfuscated"] = False
        stats[method_name]["skipped_due_to_register"] = True
        return method_blocks

    if not safe_to_extend and new_reg_index == 4:
        stats[method_name]["obfuscated"] = False
        stats[method_name]["skipped_due_to_register"] = True
        return method_blocks

    new_reg = f"v{new_reg_index}"

    # If we're extending locals, update it
    if safe_to_extend and entry_block:
        entry_block["register_info"]["locals"] = str(locals_count + 1)

    new_blocks = []
    label_counter = 0
    for block in blocks:
        modified_block = copy.deepcopy(block)
        new_instructions = []

        for instr in block["instructions"]:
            if instr.strip().startswith("goto"):
                match = re.search(r'goto(?:/\d+)?\s+:(\S+)', instr)
                if not match:
                    new_instructions.append(instr)
                    continue
                target_label = match.group(1)

                # Inline opaque predicate logic

                dummy_label_false = f"fake_false_{label_counter}"
                dummy_continue = f"fake_continue_{label_counter}"
                label_counter += 1
                
                new_instructions.append(f"const/16 {new_reg}, 0x1F")                        # {new_reg} = 31
                new_instructions.append(f"shl-int/lit8 {new_reg}, {new_reg}, 2")            # {new_reg} = 31 << 2 = 124
                new_instructions.append(f"add-int/lit8 {new_reg}, {new_reg}, 7")            # {new_reg} = 124 + 7 = 131
                new_instructions.append(f"xor-int/lit8 {new_reg}, {new_reg}, 0x2")          # {new_reg} = 131 ^ 2 = 129
                new_instructions.append(f"mul-int/lit8 {new_reg}, {new_reg}, 5")            # {new_reg} = 129 * 5 = 645
                new_instructions.append(f"shl-int/lit8 {new_reg}, {new_reg}, 1")            # {new_reg} = 645 << 1 = 1290
                new_instructions.append(f"add-int/lit16 {new_reg}, {new_reg}, 11981")       # {new_reg} = 1290 + 11981 = 13271
                new_instructions.append(f"shl-int/lit8 {new_reg}, {new_reg}, 2")            # {new_reg} = 13271 << 2 = 53084
                new_instructions.append(f"add-int/lit16 {new_reg}, {new_reg}, 1267")        # {new_reg} = 53084 + 1267 = 54351
                new_instructions.append(f"xor-int/lit16 {new_reg}, {new_reg}, 0x1234")      # {new_reg} = 54351 ^ 0x1234 = 0x2FA0B
                new_instructions.append(f"if-gez {new_reg}, :{target_label}")        # opaque branch


                new_instructions.append(f"const/16 {new_reg}, 0x3A")                  # {new_reg} = 58
                new_instructions.append(f"shl-int/lit8 {new_reg}, {new_reg}, 3")             # {new_reg} = 58 << 3 = 464
                new_instructions.append(f"xor-int/lit16 {new_reg}, {new_reg}, 0x55AA")       # {new_reg} ^= 21930 → misleading high value
                new_instructions.append(f"add-int/lit16 {new_reg}, {new_reg}, 1234")         # confuse with weird constant
                new_instructions.append(f"rem-int/lit8 {new_reg}, {new_reg}, 7")             # modulo – hard to track
                new_instructions.append(f"mul-int/lit8 {new_reg}, {new_reg}, 19")            # multiply again
                new_instructions.append(f"or-int/lit16 {new_reg}, {new_reg}, 0x3333")        # OR with a pattern
                new_instructions.append(f"and-int/lit16 {new_reg}, {new_reg}, 0x7FFF")       # limit range
                # Dummy branch (always false, but confuses control flow)
                new_instructions.append(f"if-lez {new_reg}, :{dummy_label_false}")
                new_instructions.append(f"goto :{dummy_continue}")
                new_instructions.append(f":{dummy_label_false}")
                new_instructions.append(f"const/4 {new_reg}, 0x0")                    # fake reset
                new_instructions.append(f"goto :{dummy_continue}")
                new_instructions.append(f":{dummy_continue}")
                # Dummy method call (pretend to use value, dead-end)
                new_instructions.append(f"invoke-static {{{new_reg}}}, Ljava/lang/Integer;->toHexString(I)Ljava/lang/String;")
                # Final fake math to pad block
                new_instructions.append(f"add-int/lit8 {new_reg}, {new_reg}, 3")
                new_instructions.append(f"xor-int/lit8 {new_reg}, {new_reg}, 0x3")
                new_instructions.append(f"shl-int/lit8 {new_reg}, {new_reg}, 1")
                new_instructions.append(f"goto :{target_label}")

                #new_instructions.extend(generate_opaque_predicate(new_reg, target_label, dummy_label_false, dummy_continue)) 
            else:
                new_instructions.append(instr)

        modified_block["instructions"] = new_instructions
        # Since we are no longer modifying CFG, remove next_block if present
        modified_block.pop("next_block", None)
        new_blocks.append(modified_block)

    method_blocks["blocks"] = new_blocks
    return method_blocks


def transform_gotos_with_opaque_blocks_grouped(json_data, stats):
    transformed_data = {"class_directives": json_data.get("class_directives", [])}
    for method, block_group in json_data.items():
        if method == "class_directives":
            continue
        transformed_data[method] = transform_method_blocks(json_data,block_group, method, stats)
    return transformed_data


def print_stats(stats):
    print(bold("\n╭────────────────────────────[ Obfuscation Summary ]────────────────────────────╮"))
    
    total_methods = len(stats)
    total_with_goto = sum(1 for s in stats.values() if s["goto_count"] > 0)
    obfuscated_methods = sum(1 for s in stats.values() if s["obfuscated"])

    for method, s in stats.items():
        if s.get("skipped_due_to_register"):
            status = yellow("⚠ skipped (unsafe registers)")
        elif s["obfuscated"]:
            status = green("✔ obfuscated")
        else:
            status = red("✘ no gotos")
        print(f" {cyan(method):40s} → {status} ({s['goto_count']} goto(s))")

    print("╰──────────────────────────────────────────────────────────────────────────────╯")

    percent_total = (obfuscated_methods / total_methods) * 100 if total_methods else 0
    percent_only_goto = (obfuscated_methods / total_with_goto) * 100 if total_with_goto else 0
    skipped_methods = sum(1 for s in stats.values() if s.get("skipped_due_to_register"))
    print(f"\n{cyan('[✓]')} Total methods: {yellow(total_methods)}")
    print(f"{cyan('[✓]')} Methods with 'goto': {yellow(total_with_goto)}")
    print(f"{cyan('[✓]')} Obfuscated methods: {green(obfuscated_methods)}")
    print(f"{cyan('[✓]')} Skipped due to no safe registers: {yellow(skipped_methods)}")


    print(f"\n{cyan('[✓]')} Obfuscation Coverage (All methods): {bold(green(f'{percent_total:.2f}%'))}")
    print(f"{cyan('[✓]')} Obfuscation Coverage (Only methods with 'goto'): {bold(cyan(f'{percent_only_goto:.2f}%'))}\n")



def main():
    if len(sys.argv) != 3:
        print("Usage: python obfuscator.py <input_cfg.json> <output_subdir>")
        return 1

    input_path = sys.argv[1]
    output_subdir = sys.argv[2]

    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return 1

    with open(input_path, "r") as infile:
        json_data = json.load(infile)

    stats = {}
    transformed = transform_gotos_with_opaque_blocks_grouped(json_data, stats)

    # Count totals before writing
    total_methods = len(stats)
    total_with_goto = sum(1 for s in stats.values() if s["goto_count"] > 0)
    obfuscated_methods = sum(1 for s in stats.values() if s["obfuscated"])

    # Save the result only if something changed (optional)
    output_dir = os.path.join("obfuscated_jsons", output_subdir)    
    os.makedirs(output_dir, exist_ok=True)

    base_name = os.path.basename(input_path)
    output_filename = f"obfuscated_{base_name}"
    output_path = os.path.join(output_dir, output_filename)

    with open(output_path, "w") as outfile:
        json.dump(transformed, outfile, indent=2)

    
    stats_file = os.environ.get("STATS_FILE")
    if stats_file:
        try:
            with open(stats_file, "w") as f:
                json.dump(stats, f)
        except Exception as e:
            print(f"[!] Failed to write stats to file: {e}")

    print(f"{bold(green('[✓]'))} Transformed CFG written to {yellow(output_path)}\n")

    # 💡 Custom return code 0xd100 if NO obfuscation was applied
    if obfuscated_methods == 0:
        return 100
    print_stats(stats)
    return 0



if __name__ == "__main__":
    sys.exit(main())
