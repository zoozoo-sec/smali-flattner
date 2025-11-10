import sys
from antlr4 import *
from smali_parser.SmaliLexer import SmaliLexer
from smali_parser.SmaliParser import SmaliParser
from smali_parser.SmaliParserListener import SmaliParserListener
from SmaliInfoExtractor import *
from antlr4.tree.Trees import Trees

import os 

def parse_smali_file(smali_file):
    # Parse the file
    input_stream = FileStream(smali_file, encoding='utf-8')
    lexer = SmaliLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SmaliParser(stream)
    tree = parser.smali_file()

    # Build CFG
    cfg_builder = CFGBuilder()
    walker = ParseTreeWalker()

    walker.walk(cfg_builder, tree)
    #print(Trees.toStringTree(tree, parser.ruleNames))


    # Generate JSON output
    visualizer = CFGVisualizer(
        cfg_builder.cfg,
        cfg_builder.block_methods,
        cfg_builder.method_start_indices,
        cfg_builder.method_end_indices,
        cfg_builder.class_directives # Pass the collected directives
    )
    
    return(visualizer.generate_json())

def store_to_file(output, smali_file, output_subdir):
    basename = os.path.basename(smali_file)
    filename = os.path.splitext(basename)[0] + ".json"
    # Construct the full output directory path
    output_dir = os.path.join("json_outputs", output_subdir)
    os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists
    output_path = os.path.join(output_dir, filename)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=1)
    print(f"[+] CFG Object written to: {output_path}")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python Engine.py <inputsmali> <output_subdir>")
        sys.exit(1)

    smali_file = sys.argv[1]
    output_subdir = sys.argv[2]
    output = parse_smali_file(smali_file)
    #print(output)
    store_to_file(json.loads(output),smali_file,output_subdir)
   


# need grammer    .field and other .types 
# need to look at $NET thing in synthetic
# need to resolve parameters problem in method definition