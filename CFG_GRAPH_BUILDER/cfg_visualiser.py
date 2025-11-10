import json
import os
import re
import sys
import html
from graphviz import Digraph

# ──────────────────────────────────────────────
# Aesthetic CLI Styling
# ──────────────────────────────────────────────

def green(text): return f"\033[92m{text}\033[0m"
def bold(text): return f"\033[1m{text}\033[0m"
def success(text): return green(bold(f"[✓] {text}"))

# ──────────────────────────────────────────────
def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def get_block_color(block):
    if block.get("is_entry"):
        return "#d2f8d2"  # entry block - light green
    elif block.get("is_exit"):
        return "#f8d2d2"  # exit block - light red
    elif block.get("label"):
        return "#fffac8"  # labeled block - light yellow
    else:
        return "white"   # default

def render_cfg_for_method(method_name, method_data, output_dir):
    dot = Digraph(format='png')
    dot.attr(rankdir='TB')
    dot.attr('node', shape='plaintext', fontname='Helvetica')
    label_to_block_id = {}

    for block in method_data['blocks']:
        block_id = str(block['id'])

        label_html = """<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
        """

        if block.get('label'):
            label_html += f"""<TR><TD BGCOLOR="#fffac8"><B>Label</B></TD></TR>"""
            if isinstance(block['label'], list):
                for label in block['label']:
                    label_html += f"""<TR><TD BGCOLOR="#fffac8">{html.escape(label)}</TD></TR>"""
            else:
                label_html += f"""<TR><TD BGCOLOR="#fffac8">{html.escape(str(block['label']))}</TD></TR>"""

        if block.get('instructions'):
            label_html += f"""<TR><TD BGCOLOR="#f0f8ff"><B>Instructions</B></TD></TR>"""
            for instr in block['instructions']:
                label_html += f"""<TR><TD BGCOLOR="#f0f8ff">{html.escape(instr)}</TD></TR>"""

        if block.get('directives'):
            for directive in block['directives']:
                label_html += f"""<TR><TD BGCOLOR="#f5f5f5">{html.escape(directive)}</TD></TR>"""

        if not block.get('instructions') and not block.get('label') and not block.get('directives'):
            label_html += """<TR><TD>(empty)</TD></TR>"""

        label_html += "</TABLE>>"

        dot.node(block_id, label=label_html, style="filled", fillcolor=get_block_color(block))

    for block in method_data['blocks']:
        visited = set()
        src = str(block['id'])

        for edge in block.get('next_block', []):
            dst = str(edge['target_block'])
            etype = edge.get('type', 'next')
            value = edge.get('value')

            if etype.lower() in ['true', 'false']:
                dot.edge(src, dst, label=etype, color='red', fontcolor='red')
            elif value:
                dot.edge(src, dst, label=value, color='blue', fontcolor='blue')
            else:
                dot.edge(src, dst, color='black')

            current = edge.get('target_block')
            visited.add(current)

            while True:
                if current in visited:
                    break
                visited.add(current)

                next_block = next((b for b in method_data['blocks'] if b['id'] == current), None)
                if not next_block or not next_block.get('next_block'):
                    break

                next_edge = next_block['next_block'][0]
                next_dst = str(next_edge['target_block'])
                dot.edge(str(current), next_dst, style='dashed', color='gray')

                current = next_edge['target_block']

    safe_method_name = sanitize_filename(method_name)
    output_dir = os.path.join(os.getcwd(),output_dir)
    output_path = os.path.join(output_dir, f"{safe_method_name}")
    dot.render(output_path, cleanup=True)
    print(success(f"Saved graph: {output_path}"))

def render_cfg(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)

    base_name = os.path.basename(json_path)
    name_no_suffix = base_name.replace('_restructured.json', '')
    output_dir = os.path.join("graphs", name_no_suffix)
    os.makedirs(output_dir, exist_ok=True)

    for key in data:
        if key == "class_directives":
            continue
        render_cfg_for_method(key, data[key], output_dir)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python cfg_visualiser.py <method_restructured.json>")
        sys.exit(1)

    jsonfile = sys.argv[1]
    render_cfg(jsonfile)
