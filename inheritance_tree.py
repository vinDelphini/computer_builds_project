import ast
import os
from graphviz import Digraph

def extract_inheritance(file_path):
    """Extracts class inheritance information from a Python file."""
    with open(file_path, "r") as file:
        tree = ast.parse(file.read(), filename=file_path)

    classes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            # Extract class name and base classes
            class_name = node.name
            bases = [base.id for base in node.bases if isinstance(base, ast.Name)]
            classes.append((class_name, bases))
    return classes

def build_inheritance_tree(directory):
    """Builds an inheritance tree from Python files in a directory."""
    inheritance_tree = []
    
    # Traverse the directory to find all Python files
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                inheritance_tree.extend(extract_inheritance(file_path))
    
    return inheritance_tree

def visualize_inheritance_tree(inheritance_tree):
    """Visualizes the inheritance tree using graphviz with customization."""
    dot = Digraph(comment='Class Inheritance Tree')
    
    # Set global attributes for nodes and edges
    # DOCUMENTATION: https://graphviz.readthedocs.io/en/stable/manual.html#styling
    dot.attr('node', shape='box', style='filled', color='lightblue', fontname='Arial', fontsize='12')
    dot.attr('edge', color='gray', arrowhead='open', style='line')

    # Add nodes and edges based on class inheritance
    for class_name, bases in inheritance_tree:
        dot.node(class_name, class_name, color='lightgreen')  # Customize individual nodes
        for base in bases:
            dot.node(base, base, color='lightcoral')  # Different color for base classes
            dot.edge(base, class_name, label='inherits')  # Add label to edges

    # Customize graph layout
    dot.graph_attr['rankdir'] = 'LR'  # Left to Right layout instead of Top to Bottom
    dot.render('inheritance_tree', format='png', view=True)

# Specify the directory containing your Python project files
project_directory = '/home/vin/OOP_object_oriented_programming/computer_builds_project/app/models'

# Extract and visualize the class inheritance
inheritance_tree = build_inheritance_tree(project_directory)
visualize_inheritance_tree(inheritance_tree)
