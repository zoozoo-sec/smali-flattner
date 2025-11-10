from smali_parser.SmaliParserListener import SmaliParserListener
import json
import re
from collections import defaultdict



class Block:
    def __init__(self):
        self.instructions = []
        self.label = None
        self.is_entry = False
        self.is_exit = False
        self.directives = []
        self.is_method_start = False
        self.register_info = {} 
        self.register_types = {}
        self.current_block = None

class CFG:
    def __init__(self):
        self.blocks = []
        self.edges = set()
        self.entry_block = 0
        self.in_switch = False
        self.switch_instructions = []
        self.in_annotation = False
        self.annotation_buffer = []
        

class CFGBuilder(SmaliParserListener):
    def __init__(self):
        self.in_param_annotation = False
        self.current_block = Block()
        self.blocks = []
        self.method_label_maps = {}
        self.cfg = CFG()
        self.current_method = None
        self.class_directives = []
        self.method_start = True
        self.method_start_indices = {}
        self.method_end_indices = {}
        self.block_methods = {}
        self.method_label_maps = {} 
        self.inferred_types_per_method = defaultdict(lambda: defaultdict(set))
        self.annotation_set = set()

    def enterClassDirective(self, ctx):
        tokens = [child.getText() for child in ctx.getChildren()]
        directive_text = ' '.join(tokens).strip()
        self.class_directives.append(directive_text)
        # Create a new block for class directives if needed
        if self.current_block.instructions or self.current_block.directives:
            self.blocks.append(self.current_block)
            self.current_block = Block()
        #self.current_block.directives.append(directive_text)
        self.current_block.is_class_start = True

    def enterSuperDirective(self, ctx):
        tokens = [child.getText() for child in ctx.getChildren()]
        directive_text = ' '.join(tokens).strip()
        self.class_directives.append(directive_text)
        self.current_block.directives.append(directive_text)

    def enterSourceDirective(self, ctx):
        # ONLY store in class_directives, not in blocks
        source_text = ctx.getText()
        self.class_directives.append(source_text)
        
        # Start new block if needed (without adding source again)
        if self.current_block.directives or self.current_block.instructions:
            self.blocks.append(self.current_block)
            self.current_block = Block()

    def enterFieldDirective(self, ctx):
        tokens = [child.getText() for child in ctx.getChildren()]
        field_text = ' '.join(tokens).strip()
        self.class_directives.append(field_text)

    def enterImplementsDirective(self, ctx):
        tokens = [child.getText() for child in ctx.getChildren()]
        directive_text = ' '.join(tokens).strip()
        self.class_directives.append(directive_text)
        #self.current_block.directives.append(directive_text)

    def enterLocalEndDirective(self, ctx):
        tokens = [child.getText() for child in ctx.getChildren()]
        end_local_text = ' '.join(tokens).strip()
        self.current_block.instructions.append(end_local_text)
            
    def exitLocalDirective(self, ctx):
        tokens = [child.getText() for child in ctx.getChildren()]
        end_local_text = ' '.join(tokens).strip()
        self.current_block.instructions.append(end_local_text)
            
    def enterLineDirective(self, ctx):
        tokens = [child.getText() for child in ctx.getChildren()]
        field_text = ' '.join(tokens).strip()
        self.current_block.instructions.append(field_text)
    
    def enterCatchDirective(self, ctx):

        try:
            exception_type = ctx.catchExceptionType().getText()
            from_label = ctx.catchFromLabel().getText()
            to_label = ctx.catchToLabel().getText()
            handler_label = ctx.catchGotoLabel().getText()

            formatted = f".catch {exception_type} {{ {from_label} .. {to_label} }} {handler_label}"
            self.current_block.instructions.append(formatted)
        except Exception as e:
            print(f"[!] Failed to parse .catch directive: {e}")


    def enterCatchAllDirective(self, ctx):
        try:
            from_label = ctx.catchFromLabel().getText()
            to_label = ctx.catchToLabel().getText()
            handler_label = ctx.catchGotoLabel().getText()

            formatted = f".catchall {{ {from_label} .. {to_label} }} {handler_label}"
            self.current_block.instructions.append(formatted)
        except Exception as e:
            print(f"[!] Failed to parse .catchall directive: {e}")


    def enterAnnotationDirective(self, ctx):
        self.in_annotation = True
        self.annotation_buffer = []

        # Rebuild .annotation header with space
        annotation_kw = ctx.ANNOTATION_DIRECTIVE().getText()  # ".annotation"
        scope = ctx.annotationScope().getText()               # "runtime"
        atype = ctx.annotationType().getText()                # "Lkotlin/Metadata;"
        header = f"{annotation_kw} {scope} {atype}"
        self.annotation_buffer.append(header)


    def format_annotation_lines(self, lines):
        formatted = []
        inside_brace_block = False

        for line in lines:
            stripped = line.strip()

            # Detect block start and end
            if "{" in stripped and not stripped.endswith("}"):
                inside_brace_block = True

            if "}" in stripped:
                inside_brace_block = False

            # Smali annotation values never require semicolons
            if (
                stripped.startswith(".end")
                or stripped.startswith(".annotation")
                or re.match(r'^\w+\s*=\s*.+$', stripped)  # key = value, even with {}
                or inside_brace_block
                or stripped.endswith("}")
                or stripped.endswith("{")
            ):
                formatted.append(stripped)
            else:
                # Add semicolon only for real directives like class/method annotations outside key-value pairs
                formatted.append(stripped + ";")

        return formatted




    def exitAnnotationDirective(self, ctx):
        try:
            if (
                "EnclosingMethod;" in self.annotation_buffer[0]
                and len(self.annotation_buffer) >= 2
            ):
                
                value_line_index = None
                for i, line in enumerate(self.annotation_buffer[1:], start=1):
                    if line.strip().startswith("value"):
                        value_line_index = i
                        break

                if value_line_index is not None:
                    # Extract class and method part
                    value_line = self.annotation_buffer[value_line_index].strip()
                    class_and_method = value_line.split("=", 1)[1].strip()

                    if "->" in class_and_method:
                        class_part, method_part = class_and_method.split("->", 1)
                    else:
                        class_part = class_and_method
                        method_part = ""

                    if not class_part.endswith(";"):
                        class_part += ";"

                    # Collect method descriptor safely from the following lines (exclude '.end annotation')
                    method_lines = self.annotation_buffer[value_line_index + 1:]
                    method_lines = [line.strip() for line in method_lines if ".end annotation" not in line]

                    full_method = method_part + ''.join(method_lines)

                    # Normalize init or clinit if malformed
                    if full_method.startswith("init>"):
                        full_method = "<init>" + full_method[len("init>"):]
                    elif full_method.startswith("clinit>"):
                        full_method = "<clinit>" + full_method[len("clinit>"):]

                    # Avoid appending 'V' if a return type already exists
                    # Smali method signatures always have format: (params)return_type
                    if re.match(r'.*\)\s*$', full_method):
                        full_method += "V"  # default return type

                    fixed_value = f"value = {class_part}->{full_method}"

                    self.annotation_buffer = [
                        self.annotation_buffer[0],
                        fixed_value,
                        ".end annotation"
                    ]
                else:
                    self.annotation_buffer.append(".end annotation")

        except Exception as e:
            print(f"[!] Failed to fix EnclosingMethod annotation format: {e}")
            self.annotation_buffer.append(".end annotation")

        # Make sure only one `.end annotation`
        if not self.annotation_buffer[-1].strip() == ".end annotation":
            self.annotation_buffer.append(".end annotation")

        formatted = "\n".join(self.format_annotation_lines(self.annotation_buffer))


        if self.in_param_annotation:
            # annotation belongs to a .param – already handled in instructions
            pass

        elif self.current_method:
            self.current_block.instructions.append(formatted)
        else:
            if formatted not in self.annotation_set:
                self.class_directives.append(formatted)
                self.annotation_set.add(formatted)

        # Reset
        self.in_annotation = False
        self.annotation_buffer = []
        self.in_param_annotation = False

    
    def enterParamDirective(self, ctx):
        self.in_param_annotation = True  # Mark that we're inside a .param annotation

        param_reg = ctx.registerIdentifier().getText()
        param_line = f".param {param_reg}"
        lines = [param_line]

        annotation_started = False

        for child in ctx.children:
            text = child.getText().strip()

            # Handle annotation start
            if text.startswith(".annotation"):
                annotation_started = True
                # Insert space between 'runtime' and type
                match = re.match(r"\.annotation\s*(runtime)?(.*)", text)
                if match:
                    runtime_prefix = match.group(1).strip() + " " if match.group(1) else ""
                    annotation_type = match.group(2).strip()
                    lines.append(f"    .annotation {runtime_prefix}{annotation_type}")
                continue

            # Handle annotation content like: name = "version"
            if "=" in text and annotation_started:
                key, val = map(str.strip, text.split("=", 1))
                lines.append(f"        {key} = {val}")
                continue

            # Handle .end annotation
            if text.startswith(".end annotation"):
                lines.append("    .end annotation")
                annotation_started = False
                continue

        # Final line
        lines = [l.replace(".end param","").replace(";",";\n").replace(".end annotation","\n.end annotation") for l in lines]
        lines.append(".end param")

        # Save the instruction
        formatted = "\n".join(lines)
        self.current_block.instructions.append(formatted)


    def exitParamDirective(self, ctx):
        self.in_param_annotation = False





    def exitAnnotationField(self, ctx):
        # Rebuild each field line like: d1 = { "..." }
        if self.in_annotation:
            field_text = ctx.getText()

            # Add spacing around '=' and between values
            field_text = field_text.replace('=', ' = ')
            field_text = re.sub(r',(?=\S)', ', ', field_text)  # Fix commas
            field_text = re.sub(r'{\s*', '{ ', field_text)
            field_text = re.sub(r'\s*}', ' }', field_text)

            self.annotation_buffer.append(field_text)
            
    def enterArrayDataDirective(self, ctx):
        # Start a new block if needed
        if self.current_block.instructions or self.current_block.directives:
            self.blocks.append(self.current_block)
            self.current_block = Block()
        
        # Mark this as an array data block
        self.current_block.is_array_data = True
        
        # Get the element width (2 for short, 4 for int, etc.)
        element_width = ctx.numericLiteral().getText()
        self.current_block.instructions.append(f".array-data {element_width}")
        
        # Store array data entries
        self.current_block.array_data_entries = []
        for entry in ctx.arrayDataEntry():
            value = entry.numericLiteral().getText()
            if entry.IDENTIFIER():
                suffix = entry.IDENTIFIER().getText()  # 's' for short, etc.
                value += suffix
            self.current_block.array_data_entries.append(value)

    def exitArrayDataDirective(self, ctx):
        # Add all array data entries to the block
        for entry in self.current_block.array_data_entries:
            self.current_block.instructions.append(entry)
        
        # Add the end directive
        self.current_block.instructions.append(".end array-data")
        
        # Add to blocks if it's part of a method
        if self.current_method:
            self.blocks.append(self.current_block)
            self.current_block = Block()
        else:
            # If not in a method, add to class directives
            array_data = "\n".join([".array-data"] + 
                                self.current_block.array_data_entries + 
                                [".end array-data"])
            self.class_directives.append(array_data)
            self.current_block = Block()

    def exitEndFieldDirective(self, ctx):
        directive = ' '.join(child.getText() for child in ctx.getChildren())
        self.class_directives.append(directive)
        self.in_field = False

    def exitInstruction(self, ctx):
        tokens = [child.getText() for child in ctx.getChildren()]
        raw = "".join(tokens).strip()
        
        # Decide which instruction formatting to use
        if raw.startswith("invoke-") and "->" in raw and "(" in raw:
            instr = raw  # DO NOT touch invoke lines
        elif raw.startswith("const-string") or raw.startswith("const-string/jumbo"):
            
            instr = re.sub(r'^(const-string(?:/jumbo)?)([vp]\d+)', r'\1 \2', raw)
        else:
            instr = " ".join(tokens).strip()
            instr = re.sub(r'^([a-z][a-z0-9/-]+)([vp]\d+)', r'\1 \2', instr)  # 👈 ADD THIS LINE
            instr = re.sub(r'\s*([{},\[\]])\s*', r'\1', instr)
            instr = re.sub(r'(?<![/\$])(\b(p\d+|v\d+)\b)', r' \1', instr)
            instr = re.sub(r'(v\d+|p\d+)(,)', r'\1\2 ', instr)
            instr = re.sub(r'(return|move-result|add-int/lit8|sub-int|if-[a-z]+)(v\d+|p\d+)', r'\1 \2', instr)
            instr = re.sub(r'(goto)(:)', r'\1 \2', instr)
            instr = re.sub(r'(if-[a-z]+)(p\d+|v\d+),', r'\1 \2,', instr)
            instr = re.sub(r'(if-[a-z]+ [pv\d]+,)([pv\d]+)', r'\1 \2', instr)
            instr = re.sub(r'(,):', r', :', instr)
            instr = re.sub(r'\s+', ' ', instr).strip()

        # Save .registers info
        if instr.startswith(".registers"):
            try:
                count = int(instr.split()[-1])
                self.current_block.register_info["registers"] = count
            except:
                pass

        # Handle method entry
        if self.method_start:
            if self.current_block.instructions or self.current_block.directives:
                self.blocks.append(self.current_block)
                self.current_block = Block()
            self.method_start = False

        # Branching instructions form their own block
        if instr.startswith(('if-', 'goto', 'return', 'sparse-switch', 'packed-switch')):
            if self.current_block.instructions:
                self.blocks.append(self.current_block)
                self.current_block = Block()

            self.current_block.instructions.append(instr)
            self.blocks.append(self.current_block)
            self.current_block = Block()
        else:
            self.current_block.instructions.append(instr)

        
    def enterLocalsDirective(self, ctx):
        locals_count = ctx.numericLiteral().getText()
        self.current_block.register_info["locals"] = locals_count

    def enterRegistersDirective(self, ctx):
        registers_count = ctx.numericLiteral().getText()
        self.current_block.register_info["registers"] = registers_count

    def enterLineLabel(self, ctx):
        label_name = ctx.label().labelName().getText()

        if self.current_block.instructions or self.current_block.directives or self.current_block.label:
            self.blocks.append(self.current_block)  
            self.current_block = Block()

        self.current_block.label = label_name

        # 🛑 Safe guard
        if self.current_method not in self.method_label_maps:
            self.method_label_maps[self.current_method] = {}  # prevent crash

        self.method_label_maps[self.current_method][label_name] = len(self.blocks)


   
          

    def enterMethodDirective(self, ctx):
        self.label_map = {}  # Reset for this method
        self.method_label_maps[self.current_method] = self.label_map
        method_name = ctx.methodDeclaration().methodSignature().methodIdentifier().getText()
        modifiers = [mod.getText() for mod in ctx.methodDeclaration().methodModifier()]

        if "synthetic" in modifiers:
            method_name = "synthetic constructor " + method_name
        elif "constructo" in modifiers:
            method_name = "constructor " + method_name
        else: 
            pass

        
        self.current_method = method_name
        self.method_start = True
        self.current_block.is_entry = True
        self.current_block.is_method_start = True

        method_decl = ctx.methodDeclaration()
        method_sig = method_decl.methodSignature()
        modifiers = [mod.getText() for mod in ctx.methodDeclaration().methodModifier()]
        modifier_str = ' '.join(modifiers).strip()
        method_text = ctx.methodDeclaration().methodSignature().getText()

        self.current_block.directives.append(f".method {modifier_str} {method_text}")
            
        self.method_start_indices[method_name] = len(self.blocks)
        self.block_methods[len(self.blocks)] = method_name

    def exitMethodDirective(self, ctx):
        
        # Add .end method to current block
        self.current_block.directives.append(".end method")
        self.current_block.is_exit = True
        
        # Add current block if it has content
        if self.current_block.instructions or self.current_block.directives or self.current_block.label:
            self.blocks.append(self.current_block)
            
            # Mark this as the method's exit block
            if self.current_method:
                self.method_end_indices[self.current_method] = len(self.blocks) - 1
        
        self.cfg.method_label_maps = self.method_label_maps
        self._build_cfg_edges()
        self._propagate_method_names()
        self.method_start = False
        self.current_method = None
        self.current_block = Block()

    def enterPackedSwitchDirective(self, ctx):
        self.in_switch = True
        self.switch_instructions = [".packed-switch"]
        
    def exitPackedSwitchDirective(self, ctx):
        self.switch_instructions = []
        base = ctx.getChild(1).getText()
        self.switch_instructions.append(f".packed-switch {base}")

        for i in range(2, ctx.getChildCount() - 1):
            child = ctx.getChild(i)
            line = child.getText().strip()
            matches = re.findall(r':\w+', line)
            for match in matches:
                self.switch_instructions.append(match)
        self.switch_instructions.append(".end packed-switch")

        if self.current_block.instructions or self.current_block.directives or self.current_block.label:
            self.blocks.append(self.current_block)
            self.current_block = Block()

        self.current_block.instructions = self.switch_instructions[:]
        current_idx = len(self.blocks)
        self.blocks.append(self.current_block)
        self.block_methods[current_idx] = self.current_method
        self.current_block = Block()
        self.in_switch = False
        self.switch_instructions = []

    def enterSparseSwitchDirective(self, ctx):
        self.in_switch = True
        self.switch_instructions = [".sparse-switch"]

    def exitSparseSwitchDirective(self, ctx):
        for child in ctx.getChildren():
            line = child.getText().strip()
            if line in [".sparse-switch", ".end sparse-switch"]:
                continue  
            if '->' in line:
                line = line.replace('->', ' -> ')
            self.switch_instructions.append(line)
        self.switch_instructions.append(".end sparse-switch")

        if self.current_block.instructions or self.current_block.directives:
            # Not empty → start a new block for switch
            self.blocks.append(self.current_block)
            self.current_block = Block()

        # Now use current_block for the switch
        self.current_block.instructions = self.switch_instructions[:]

        current_idx = len(self.blocks)
        self.blocks.append(self.current_block)
        self.block_methods[current_idx] = self.current_method

        # Reset current_block for next content
        self.current_block = Block()
        self.in_switch = False
        self.switch_instructions = []

    def _build_cfg_edges(self):
        self.cfg.edges = set()  # Clear any previously stored edges
        self.cfg.blocks = self.blocks
        self.cfg.label_map = self.label_map


        for idx, block in enumerate(self.blocks):
            if block.label:
                method = self.block_methods.get(idx)
                if method not in self.method_label_maps:
                    self.method_label_maps[method] = {}
                self.method_label_maps[method][block.label] = idx

        for i, block in enumerate(self.blocks):
            if block.instructions:
                last_instr = block.instructions[-1]
                clean_instr = re.sub(r'<.*?>', '', last_instr).strip()

                # Handle conditional branches
                if clean_instr.startswith('if-'):
                    # True branch
                    if ':' in clean_instr:
                        target_label = clean_instr.split(':')[-1].strip()
                        method_name = self.block_methods.get(i)
                        label_map = self.method_label_maps.get(method_name, {})

                        if target_label in label_map:
                            target_block = label_map[target_label]

                            # Safety: prevent cross-method jumps
                            if self.block_methods.get(i) == self.block_methods.get(target_block):
                                self.cfg.edges.add((i, target_block))
                    
                    # False branch (fall-through)
                    if i + 1 < len(self.blocks):
                        false_block = i + 1
                        self.cfg.edges.add((i, false_block))

                # Handle unconditional jump
                elif clean_instr.startswith('goto'):
                    if ':' in clean_instr:
                        target_label = clean_instr.split(':')[-1].strip()
                        method_name = self.block_methods.get(i)
                        label_map = self.method_label_maps.get(method_name, {})

                        if target_label in label_map:
                            target_block = label_map[target_label]

                            # Safety: prevent cross-method jumps
                            if self.block_methods.get(i) == self.block_methods.get(target_block):
                                self.cfg.edges.add((i, target_block))

                elif clean_instr.startswith('packed-switch'):
                    # Extract the label like ":pswitch_data_0"
                    match = re.search(r':(\w+)', clean_instr)
                    if match:
                        target_label = match.group(1)
                        method_name = self.block_methods.get(i)
                        label_map = self.method_label_maps.get(method_name, {})

                        # Get the block where :pswitch_data_0 is defined
                        if target_label in label_map:
                            switch_block_index = label_map[target_label]

                            # ✅ Add edge from packed-switch to the switch table block
                            self.cfg.edges.add((i, switch_block_index))

                            # Get the switch table block
                            switch_block = self.blocks[switch_block_index]

                            # Extract all switch case labels like :pswitch_0, :pswitch_1
                            switch_targets = []
                            for instr in switch_block.instructions:
                                matches = re.findall(r':(\w+)', instr)
                                switch_targets.extend(matches)

                            for label in switch_targets:
                                if label in label_map:
                                    target_block = label_map[label]
                                    # ✅ Add edges from packed-switch block to each target block
                                    self.cfg.edges.add((i, target_block))

                elif clean_instr.startswith('sparse-switch'):
                    match = re.search(r':(\w+)', clean_instr)
                    if match:
                        target_label = match.group(1)
                        method_name = self.block_methods.get(i)
                        label_map = self.method_label_maps.get(method_name, {})

                        if target_label in label_map:
                            switch_block_index = label_map[target_label]
                            self.cfg.edges.add((i, switch_block_index))  # link to data block

                            switch_block = self.blocks[switch_block_index]

                            # Parse the sparse-switch values and targets
                            for instr in switch_block.instructions:
                                if '->' in instr:
                                    try:
                                        value_part, label_part = instr.split('->')
                                        value = value_part.strip()
                                        label = label_part.strip().lstrip(':')
                                        if label in label_map:
                                            target_block = label_map[label]
                                            # Add edge with value as annotation (handled during visualization)
                                            self.cfg.edges.add((i, target_block))
                                            # Also store a hint so visualizer can later access it (optional)
                                            if not hasattr(self.cfg, "sparse_edges_info"):
                                                self.cfg.sparse_edges_info = {}
                                            self.cfg.sparse_edges_info[(i, target_block)] = value
                                    except ValueError:
                                        continue  # malformed line


                # Normal flow (fall-through)
                elif i + 1 < len(self.blocks):
                    self.cfg.edges.add((i, i + 1))

            else:
                # No instructions (directive/register-only block)
                if i + 1 < len(self.blocks):
                    self.cfg.edges.add((i, i + 1))



    def _verify_edges(self):
        for i, block in enumerate(self.blocks):
            if not block.instructions:
                continue
            last_instr = block.instructions[-1]
            outgoing = [e for e in self.cfg.edges if e[0] == i]
            
            if last_instr.startswith('if-'):
                assert len(outgoing) == 2, f"Conditional at block {i} has {len(outgoing)} edges"
            elif last_instr.startswith('goto'):
                assert len(outgoing) == 1, f"Goto at block {i} has {len(outgoing)} edges"

    def _propagate_method_names(self):
        """Propagate method names from entry blocks to all blocks until exit"""
        current_method = None
        for i, block in enumerate(self.blocks):
            # If this is a method entry block, start new method scope
            if block.is_entry:
                current_method = self.block_methods.get(i)
            
            # Assign current method to block
            if current_method:
                self.block_methods[i] = current_method
            
            # If this is a method exit block, end current method scope
            if block.is_exit:
                current_method = None

class CFGVisualizer:
    def __init__(self, cfg, block_methods, method_start_indices, method_end_indices, class_directives):
        self.cfg = cfg
        self.block_methods = block_methods
        self.method_start_indices = method_start_indices
        self.method_end_indices = method_end_indices
        self.class_directives = class_directives

    def _extract_class_directives(self):
        """Ensure directives only appear in one place"""
        block_directives = set()
        for block in self.cfg.blocks:
            for d in block.directives:
                if d.startswith(('.source', '.field')):
                    block_directives.add(d)
        
        # Remove from class_directives if they appear in blocks
        self.class_directives = [
            d for d in self.class_directives 
            if not (d.startswith(('.source', '.field')) and d in block_directives)
        ]

    def generate_json(self):
        self._extract_class_directives()
        cfg_data = {
            "class_directives": self.class_directives,
            "blocks": []
        }
        for i, block in enumerate(self.cfg.blocks):
            # Skip only pure directive blocks (containing only class directives)
            if not block.instructions and not block.directives and not block.label:continue 
            block_data = {
                "id": i,
                "method": self.block_methods.get(i, "None"),
                "label": block.label,
                "is_entry": block.is_entry,
                "is_exit": block.is_exit,
                "instructions": self._format_instructions(block.instructions),
                "directives": [d for d in block.directives 
                            if not d.startswith(('.class', '.super'))],
                "next_block": self._get_successors(i)
            }
            if hasattr(block, "register_info"):
                block_data["register_info"] = block.register_info

            if hasattr(block, "inferred_types"):
                block_data["inferred_types"] = block.inferred_types

            if hasattr(block, "inferred_type_sets"):
                block_data["inferred_type_sets"] = {
                    reg: list(typ_set) for reg, typ_set in block.inferred_type_sets.items()
                }
            cfg_data["blocks"].append(block_data)
        return json.dumps(cfg_data, indent=2)

    def _get_successors(self, block_idx):
        successors = []
        block = self.cfg.blocks[block_idx]
        method = self.block_methods.get(block_idx)
        method_label_map = self.cfg.method_label_maps.get(method, {})

        # --- 1. Handle packed-switch or sparse-switch labels manually ---
                # --- 1. Handle packed-switch or sparse-switch labels manually ---
                # --- 1. Handle packed-switch or sparse-switch labels manually ---
        if block.instructions and (
            block.instructions[0].startswith("sparse-switch") or
            block.instructions[0].startswith("packed-switch")
        ):
            instr = block.instructions[0]
            match = re.search(r':(\w+)', instr)
            if match:
                label = match.group(1)
                if label in method_label_map:
                    target_block = method_label_map[label]
                    successors.append({
                        "target_block": target_block,
                        "type": "jump"
                    })
        
        # --- Detect actual .sparse-switch/.packed-switch blocks ---
        if block.instructions and block.instructions[0].startswith(".sparse-switch"):
            for instr in block.instructions[1:]:
                
                instr = instr.strip()
                if instr.startswith(".end"):
                    break
                if '->' in instr:
                    parts = instr.split('->')
                    if len(parts) == 2:
                        value = parts[0].strip()
                        label_part = parts[1].strip()
                        if label_part.startswith(":"):
                            
                            label = label_part[1:]
                            if label in method_label_map:
                                target_block = method_label_map[label]
                                if not any(s["target_block"] == target_block and s.get("value") == value for s in successors):
                                    
                                    successors.append({
                                        "target_block": target_block,
                                        "value": value,
                                        "type": "jump"
                                    })

        elif block.instructions and block.instructions[0].startswith(".packed-switch"):
            for instr in block.instructions[1:]:
                instr = instr.strip()
                if instr.startswith(".end"):
                    break
                if instr.startswith(":"):
                    label = instr[1:]
                    if label in method_label_map:
                        target_block = method_label_map[label]
                        if not any(s["target_block"] == target_block for s in successors):
                            successors.append({
                                "target_block": target_block,
                                "type": "jump"
                            })



        # --- 2. Include CFG edges like fall-through or branches ---
        for src, dst in sorted([e for e in self.cfg.edges if e[0] == block_idx]):
            # Avoid adding a duplicate if it already exists
            if any(s["target_block"] == dst for s in successors):
                continue

            successors.append({
                "target_block": dst,
                "type": self._get_branch_type(src, dst)
            })
        if block.instructions:
            last_instr = block.instructions[-1].strip()
            if last_instr.startswith('goto'):
                match = re.search(r':(\w+)', last_instr)
                if match:
                    target_label = match.group(1)
                    if target_label in method_label_map:
                        target_block = method_label_map[target_label]
                        if not any(s["target_block"] == target_block for s in successors):
                            successors.append({
                                "target_block": target_block,
                                "type": "jump"
                            })
        return successors




    def _format_instructions(self, instructions):
        formatted = []
        for instr in instructions:
            # Skip string post-processing for const-string/jumbo
            if instr.startswith("const-string") or instr.startswith("const-string/jumbo"):
                formatted.append(instr)
                continue

            if '<missing' in instr:
                instr = re.sub(r'<.*?>', '', instr).strip()
                instr = instr[:5].replace(" ","") + " " + instr[5:]

            instr = instr.replace(',', ', ').replace(',  ', ', ')

            # Colon logic: only for if-*, goto etc., not const-string
            if ':' in instr and not instr.split(':')[0].endswith(' '):
                # Only fix control-flow colon formatting
                if not instr.startswith("const-"):
                    parts = instr.split(':', 1)
                    instr = f"{parts[0]} :{parts[1]}"

            formatted.append(instr)
        return formatted

    def _get_branch_type(self, src, dst):
        block = self.cfg.blocks[src]
        if not block.instructions:
            return "fall-through"

        last_instr = block.instructions[-1].split('<')[0].strip()

        if last_instr.startswith('if-'):
            if ':' in last_instr:
                target_label = last_instr.split(':')[-1].strip()
                if self.cfg.label_map.get(target_label) == dst:
                    return "True"
            if src + 1 == dst:
                return "False"
            return "True"  # fallback for malformed structures

        elif last_instr.startswith('goto'):
            return "jump"
        elif last_instr.startswith('packed-switch') or last_instr.startswith('sparse-switch'):
            return "jump"  

        return "fall-through"
