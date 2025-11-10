import json
import sys
import os
from collections import defaultdict

def green(text): return f"\033[92m{text}\033[0m"
def red(text): return f"\033[91m{text}\033[0m"
def yellow(text): return f"\033[93m{text}\033[0m"
def cyan(text): return f"\033[96m{text}\033[0m"
def bold(text): return f"\033[1m{text}\033[0m"

def should_skip_method(blocks):
    """
    Determine if a method should be skipped from flattening based on:
    - Having more than 15 local registers
    - Any register being used with multiple types
    """
    # Find entry block to get locals count
    entry_block = next((b for b in blocks if b.get("is_entry", False)), None)
    if not entry_block:
        return True  # Skip if no entry block found
    
    # Check locals count
    locals_count = 0
    if entry_block.get("register_info", {}).get("locals"):
        try:
            locals_count = int(entry_block["register_info"]["locals"])
            if locals_count > 15:
                return True
        except ValueError:
            pass
    
    # Track register types across all blocks
    register_types = defaultdict(set)
    
    # Patterns to detect type usage in instructions
    type_patterns = {
        'I': r'(int|integer|boolean|byte|char|short)',
        'J': r'(long)',
        'F': r'(float)',
        'D': r'(double)',
        'L': r'(Ljava/lang/|L[\w/$]+;)',
        '[': r'(\[)'
    }
    
    # Analyze each instruction
    for block in blocks:
        for instr in block.get("instructions", []):
            # Skip non-instruction lines
            if instr.startswith(('.', ':')):
                continue
                
            # Extract registers and their types from instruction
            parts = instr.split()
            if not parts:
                continue
                
            opcode = parts[0]
            
            # Check move operations for type conflicts
            if opcode.startswith('move'):
                if len(parts) >= 3:
                    dest_reg = parts[1]
                    src_reg = parts[2]
                    # We'd need type info here - this is simplified
                    register_types[dest_reg].add('unknown')
                    register_types[src_reg].add('unknown')
            
            # Check const operations (reveal primitive types)
            elif opcode.startswith('const'):
                if len(parts) >= 3:
                    reg = parts[1]
                    value = parts[2]
                    if value.endswith('f') or value.endswith('F'):
                        register_types[reg].add('F')
                    elif value.endswith('l') or value.endswith('L'):
                        register_types[reg].add('J')
                    elif '.' in value:
                        register_types[reg].add('D')
                    else:
                        register_types[reg].add('I')
            
            # Check array operations
            elif opcode.startswith(('array', 'aget', 'aput','new-array', 'filled-new-array')):
                if len(parts) >= 2:
                    reg = parts[1]
                    register_types[reg].add('array')
            
            # Check instance operations
            elif opcode.startswith(('iget', 'iput', 'sget', 'sput')):
                if len(parts) >= 3:
                    try:
                        # Safer field type extraction
                        field_desc = parts[2]
                        if '->' in field_desc and ':' in field_desc:
                            field_type = field_desc.split(':')[1]
                            reg = parts[1]
                            register_types[reg].add(field_type)
                    except (IndexError, AttributeError):
                        # If parsing fails, mark as unknown
                        if len(parts) >= 2:
                            reg = parts[1]
                            register_types[reg].add('unknown')
            
            # Check invoke operations
            elif opcode.startswith('invoke'):
                if len(parts) >= 2:
                    # This would need more sophisticated parsing
                    pass
    
    # Check for registers with multiple types
    for reg, types in register_types.items():
        if len(types) > 1:
            return True
    
    return False

def handle_shared_jump_targets(blocks, conditional_ids):
    """
    Detects blocks targeted by multiple conditional jumps.
    Replaces their label with a fresh list of case_{cid}_{jump_type} entries.
    """
    target_usage = defaultdict(list)
    id_to_block = {blk["id"]: blk for blk in blocks}

    # Step 1: Track which conditional blocks jump to which target blocks
    for cid in conditional_ids:
        cond_block = id_to_block.get(cid)
        for jump in cond_block.get("next_block", []):
            target_id = jump["target_block"]
            target_usage[target_id].append((cid, jump["type"].lower()))

    # Step 2: For blocks targeted by multiple conditionals
    for target_id, refs in target_usage.items():
        if len(refs) <= 1:
            continue  # Not shared, skip

        blk = id_to_block[target_id]

        # Remove any existing label (whether string or list)
        blk["label"] = []

        # Append fresh case labels
        for cid, jump_type in refs:
            new_label = f"case_{cid}_{jump_type}"
            blk["label"].append(new_label)



def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def find_conditional_blocks(blocks):
    return [
        block["id"] for block in blocks
        if any(instr.strip().startswith("if-") for instr in block.get("instructions", []))
    ]

def get_next_available_id(blocks):
    return max(block["id"] for block in blocks) 

def update_conditional_jumps(blocks, conditional_ids):
    # Build label→id map from all blocks
    label_to_id = label_to_id_map(blocks)


    id_to_block = {block["id"]: block for block in blocks}

    for cid in conditional_ids:
        cond_block = id_to_block.get(cid)
        if not cond_block:
            continue

        new_next_block = []
        for jump in cond_block.get("next_block", []):
            jump_type = jump["type"].lower()
            if jump_type == "true":
                label = f"case_{cid}_true_jumper"
            elif jump_type == "false":
                label = f"case_{cid}_false_jumper"
            else:
                continue  # unknown type

            if label in label_to_id:
                new_next_block.append({
                    "target_block": label_to_id[label],
                    "type": jump_type
                })
            else:
                raise ValueError(f"[!] Could not find label {label} for conditional block {cid}")
        
        cond_block["next_block"] = new_next_block

def patch_conditional_instruction_targets(blocks, conditional_ids):
    id_to_block = {block["id"]: block for block in blocks}

    for cid in conditional_ids:
        cond_block = id_to_block.get(cid)
        if not cond_block:
            continue

        instrs = cond_block.get("instructions", [])
        if not instrs or not instrs[0].strip().startswith("if-"):
            continue

        # Find true and false target block IDs
        true_target = None
        false_target = None
        for jump in cond_block.get("next_block", []):
            jump_type = jump["type"].lower()
            if jump_type == "true":
                true_target = jump["target_block"]
            elif jump_type == "false":
                false_target = jump["target_block"]

        if true_target is None or false_target is None:
            raise ValueError(f"[!] Conditional block {cid} missing true or false branch.")

        # Resolve labels
        true_label = id_to_block[true_target].get("label")
        false_label = id_to_block[false_target].get("label")

        if isinstance(true_label, list):
            true_label = true_label[0]
        if isinstance(false_label, list):
            false_label = false_label[0]

        if not true_label or not false_label:
            raise ValueError(f"[!] Block {cid} refers to target without label (true: {true_label}, false: {false_label})")

        # Patch the conditional instruction
        old_instr = instrs[0]
        parts = old_instr.strip().split()
        if parts[-1].startswith(":"):
            parts[-1] = f":{true_label}"
        else:
            raise ValueError(f"[!] Unexpected instruction format in block {cid}: {old_instr}")
        cond_block["instructions"][0] = " ".join(parts)

        # Append a goto for the false case
        goto_instr = f"goto :{false_label}"
        cond_block["instructions"].append(goto_instr)



def assign_labels_to_conditional_targets(blocks, conditional_ids):
    for cid in conditional_ids:
        # Find the conditional block with the given ID
        cond_block = next((b for b in blocks if b["id"] == cid), None)
        if not cond_block:
            continue  # skip if not found

        for jump in cond_block.get("next_block", []):
            target_id = jump["target_block"]
            jump_type = jump["type"].lower()
            label = f"case_{cid}_{jump_type}"

            for block in blocks:
                if block["id"] == target_id:
                    # Case 1: No label set
                    if "label" not in block or block["label"] is None:
                        block["label"] = label

                    # Case 2: Label is a string (and different)
                    elif isinstance(block["label"], str):
                        if block["label"] != label:
                            block["label"] = [block["label"], label]

                    # Case 3: Label is a list
                    elif isinstance(block["label"], list):
                        if label not in block["label"]:
                            block["label"].append(label)

def create_branch_blocks(method_name, cid, true_id, false_id, jumper_id, true_val, false_val,locals_count=None):

    if locals_count is not None and locals_count > 0:
        # Registers are v0 to vN-1 (if locals=N)
        last_register = f"v{locals_count-1}"
    else:
        # Fallback to v9 if locals count not available
        last_register = "v9"
        print(f"[!] No locals count provided for method {method_name}, using {last_register} as fallback")

    true_block = {
        "id": true_id,
        "method": method_name,
        "label": f"case_{cid}_true_jumper",
        "is_entry": False,
        "is_exit": False,
        "instructions": [
            f"const {last_register}, 0x{true_val}",
            "goto :jumper"
        ],
        "directives": [],
        "next_block": [{"target_block": jumper_id, "type": "jump"}]
    }

    false_block = {
        "id": false_id,
        "method": method_name,
        "label": f"case_{cid}_false_jumper",
        "is_entry": False,
        "is_exit": False,
        "instructions": [
            f"const {last_register}, 0x{false_val}",
            "goto :jumper"
        ],
        "directives": [],
        "next_block": [{"target_block": jumper_id, "type": "jump"}]
    }

    return true_block, false_block



def create_dispatcher_block(method_name, conditional_ids, new_id):
    switch_cases = []
    next_blocks = []
    case_value = 0

    for cid in conditional_ids:
        switch_cases.append(f"    :case_{cid}_true")
        switch_cases.append(f"    :case_{cid}_false")
        next_blocks.append({
            "target_block": -1,  # placeholder
            "type": "jump"
        })
        next_blocks.append({
            "target_block": -1,  # placeholder
            "type": "jump"
        })
        case_value += 2
    
    return {
        "id": new_id,
        "method": method_name,
        "label": "dispatcher",
        "is_entry": False,
        "is_exit": False,
        "instructions": [".packed-switch 0x0"] + switch_cases + [".end packed-switch"],
        "directives": [],
        "next_block": next_blocks  # we'll fill target_block values later
    }

def create_jumper_block(method_name, new_id, dispatcher_id,locals_count):
    if locals_count is not None and locals_count > 0:
        # Registers are v0 to vN-1 (if locals=N)
        last_register = f"v{locals_count-1}"
    else:
        # Fallback to v9 if locals count not available
        last_register = "v9"
        print(f"[!] No locals count provided for method {method_name}, using {last_register} as fallback")

    return {
        "id": new_id,
        "method": method_name,
        "label": "jumper",
        "is_entry": False,
        "is_exit": False,
        "instructions": [
            f"packed-switch {last_register}, :dispatcher"
        ],
        "directives": [],
        "next_block": [{"target_block": dispatcher_id, "type": "jump"}]
    }

def label_to_id_map(blocks):
    label_to_id = {}
    for block in blocks:
        label = block.get("label")
        if isinstance(label, str):
            label_to_id[label] = block["id"]
        elif isinstance(label, list):
            for l in label:
                label_to_id[l] = block["id"]
    return label_to_id

def fill_dispatcher_next_block(dispatcher_block, label_to_id):
    cases = [
        line.strip() for line in dispatcher_block["instructions"]
        if line.strip().startswith(":case_")
    ]

    for case_label in cases:
        if case_label in label_to_id:
            dispatcher_block["next_block"].append({
                "target_block": label_to_id[case_label],
                "type": "jump"
            })

def insert_blocks_before_endmethod(blocks, new_blocks):
    new_end = {
        "id": 0,
        "method": "",
        "label": None,
        "is_entry": False,
        "is_exit":True,
        "instructions": [],
        "directives": [
          ".end method"
        ],
        "next_block": []
    }  
    
    for i, block in enumerate(blocks):
        if ".end method" in block.get("directives", []):
            if block['label']: 
                block['directives'] = []
                block['is_exit'] = False
                new_end['id'] = block["id"] + 1
                new_end['is_exit'] = True
                new_end['method'] = block['method']
                end_block = new_end
            else: end_block = blocks.pop(i)
            # Step 1: Assign fresh IDs to new blocks
            next_id = max(b["id"] for b in blocks) + 1
            
            for nb in new_blocks:
                nb["id"] = next_id
                next_id += 1

            
            # Step 2: Build label→id mapping from updated new_blocks
            all_blocks = blocks + new_blocks
            label_to_id = label_to_id_map(all_blocks)


            # Step 3: Update placeholder target_block = -1
            for nb in new_blocks:
                for jump in nb.get("next_block", []):
                    if jump["target_block"] == -1:
                        jump["target_block"] = next_id  # .end method block

            # Step 4: Update dispatcher next_block list using resolved labels

            for nb in new_blocks:
                if nb.get("label") == "dispatcher":
                    switch_labels = [
                        line.strip() for line in nb["instructions"]
                        if line.strip().startswith(":")
                    ]
                    nb["next_block"] = []  # Clear and rebuild
                    for label in switch_labels:
                        label = label.lstrip(":")
                        if label in label_to_id:
                            nb["next_block"].append({
                                "target_block": label_to_id[label],
                                "type": "jump"
                            })
                        else:
                            raise ValueError(f"[!] Dispatcher refers to unknown label: {label}")
                    nb["next_block"].append({
                        "target_block": next_id,  # ID of .end method block
                        "type": "jump"
                    })

            # Step 5: Add .end method block back with correct ID
            end_block["id"] = next_id            
            blocks.extend(new_blocks)
            blocks.append(end_block)
            if new_end["id"] != 0:
                for i in blocks: 
                    if i["id"] == 14:
                        i['next_block'] =  [{"target_block": next_id, "type": "jump"}]
            return

    raise ValueError("'.end method' block not found.")

def process_all_methods(smali_data):
    flattened_methods = []
    skipped_complex = []
    skipped_nocond = []

    for method_name, method_obj in smali_data.items():
        if method_name == "class_directives":
            continue

        blocks = method_obj["blocks"]

        if should_skip_method(blocks):
            skipped_complex.append(method_name)
            continue

        conditional_ids = find_conditional_blocks(blocks)
        if not conditional_ids:
            skipped_nocond.append(method_name)
            continue

        # Ensure enough local registers
        entry_block = next((b for b in blocks if b.get("is_entry", False)), None)
        if entry_block:
            reginfo = entry_block.setdefault("register_info", {})
            try:
                locals_count = int(reginfo.get("locals", "0"))
                reginfo["locals"] = str(locals_count + 1)
            except ValueError:
                reginfo["locals"] = "10"

        handle_shared_jump_targets(blocks, conditional_ids)
        assign_labels_to_conditional_targets(blocks, conditional_ids)

        locals_count = None
        entry_block = next((b for b in blocks if b.get("is_entry", False)), None)
        if entry_block and entry_block.get("register_info", {}).get("locals"):
            try:
                locals_count = int(entry_block["register_info"]["locals"])
            except ValueError:
                pass

        next_id = get_next_available_id(blocks)
        dispatcher_id = next_id
        jumper_id = next_id + 1
        next_id += 2

        dispatcher = create_dispatcher_block(method_name, conditional_ids, dispatcher_id)
        jumper = create_jumper_block(method_name, jumper_id, dispatcher_id, locals_count)
        new_blocks = [dispatcher, jumper]

        switch_value = 0
        for cid in conditional_ids:
            true_blk, false_blk = create_branch_blocks(
                method_name, cid, next_id, next_id + 1, jumper_id,
                true_val=switch_value, false_val=switch_value + 1,
                locals_count=locals_count
            )
            new_blocks.extend([true_blk, false_blk])
            next_id += 2
            switch_value += 2

        insert_blocks_before_endmethod(blocks, new_blocks)
        update_conditional_jumps(blocks, conditional_ids)
        patch_conditional_instruction_targets(blocks, conditional_ids)

        flattened_methods.append(method_name)

       # ─────────────── Summary Output ───────────────
    print(bold("\n╭────────────────────────────[ Flattening Summary ]────────────────────────────╮"))

    for method in sorted(flattened_methods):
        print(f" {cyan(method):40s} → {green('✔ flattened')}")

    for method in sorted(skipped_complex):
        print(f" {cyan(method):40s} → {yellow('⚠ skipped (complex logic)')}")

    for method in sorted(skipped_nocond):
        print(f" {cyan(method):40s} → {red('✘ skipped (no conditionals)')}")

    print("╰──────────────────────────────────────────────────────────────────────────────╯")

    # Summary stats
    total_methods = len(flattened_methods) + len(skipped_complex) + len(skipped_nocond)
    total_conditional_methods = len(flattened_methods) + len(skipped_complex)
    flatten_percent_total = (len(flattened_methods) / total_methods * 100) if total_methods else 0
    flatten_percent_conditional = (len(flattened_methods) / total_conditional_methods * 100) if total_conditional_methods else 0

    print(f"\n{cyan('[✓]')} Total methods: {yellow(total_methods)}")
    print(f"{cyan('[✓]')} Methods with conditionals: {yellow(total_conditional_methods)}")
    print(f"{cyan('[✓]')} Flattened methods: {green(len(flattened_methods))}")
    print(f"{cyan('[✓]')} Skipped (complex): {yellow(len(skipped_complex))}")
    print(f"{cyan('[✓]')} Skipped (no conditionals): {red(len(skipped_nocond))}")

    print(f"\n{cyan('[✓]')} Flattening Coverage (all methods): {bold(green(f'{flatten_percent_total:.2f}%'))}")
    print(f"{cyan('[✓]')} Flattening Coverage (methods with conditionals): {bold(cyan(f'{flatten_percent_conditional:.2f}%'))}\n")

def save_json(data, output_path):
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"[+] Saved modified JSON to {output_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python inject_dispatcher.py <input_json>")
        return

    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print(f"[-] File not found: {input_path}")
        return

    smali_data = load_json(input_path)
    process_all_methods(smali_data)
    original_filename = os.path.basename(input_path)  
    injected_filename = "injected_" + original_filename  

    output_dir = os.path.join(os.getcwd(), "injected_jsons")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, injected_filename)
    save_json(smali_data, output_path)

if __name__ == "__main__":
    main()
