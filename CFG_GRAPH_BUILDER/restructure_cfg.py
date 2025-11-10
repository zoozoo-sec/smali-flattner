import json
import sys
import os
from collections import defaultdict

def restructure_cfg_by_method(filepath,output_subdir):
    with open(filepath, 'r') as f:
        data = json.load(f)

    output = {}
    output['class_directives'] = data.get('class_directives', [])

    blocks_by_id = {block['id']: block for block in data['blocks']}
    methods = defaultdict(list)

    for block in data['blocks']:
        block_id = block['id']

        # --- Step 1: If this block ends the method, remove successors ---
        if any(".end method" in directive for directive in block.get('directives', [])):
            block['next_block'] = []  # ✅ Do NOT skip grouping the block

        # --- Step 2: Refined return logic ---
        if block.get('instructions') and block.get('next_block'):
            last_instr = block['instructions'][-1].strip()
            if last_instr.startswith("return"):
                new_next_block = []

                for nb in block['next_block']:
                    target_id = nb['target_block']
                    target_block = blocks_by_id.get(target_id)

                    if not target_block:
                        continue

                    has_only_end_directive = (
                        not target_block.get('instructions') and
                        target_block.get('directives') == [".end method"]
                    )

                    if has_only_end_directive:
                        new_next_block.append(nb)
                    # else: do not include it

                block['next_block'] = new_next_block

        # ✅ Group block under its method regardless of above changes
        method_name = block['method']
        methods[method_name].append(block)

    # Output each method block group
    for method_name, blocks in methods.items():
        output[method_name] = {'blocks': blocks}

    # Construct output file path
    base_name = os.path.basename(filepath)
    name_no_ext, ext = os.path.splitext(base_name)
    output_folder = os.path.join("restructured_jsons", output_subdir) 
    #output_folder = os.path.join(os.path.dirname(filepath), 'restructured_jsons')
    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(output_folder, f"{name_no_ext}_restructured{ext}")

    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"[+] Restructured CFG written to: {output_path}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python restructure_cfg.py <path_to_json> <output_dir>")
        sys.exit(1)

    output_subdir = sys.argv[2]
    input_path = sys.argv[1]
    restructure_cfg_by_method(input_path,output_subdir)
