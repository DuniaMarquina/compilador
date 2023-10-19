import ast

source_code = '' 
with open('code-example.py', 'r') as source_file:
    for line in source_file.readlines():
        source_code += line

source_file.close()

def recursive_dump(root, dump_file):
    for node in ast.iter_child_nodes(root):
        dump_file.write(ast.dump(node))
        dump_file.write("\n\n")
        #recursive_dump(node, dump_file)

tree = ast.parse(source_code, filename='code-example.py')

with open('dumps/dump_example_python.txt', 'w') as dump_file:
    recursive_dump(tree, dump_file)