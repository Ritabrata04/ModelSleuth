import ast
from utils import get_base_class_name

def analyze_models(files):
    model_info = []
    for file in files:
        if file.endswith('.py'):
            with open(file, 'r') as f:
                tree = ast.parse(f.read())
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        for base in node.bases:
                            base_class_name = get_base_class_name(base)
                            if base_class_name in ['nn.Module', 'tf.keras.Model']:
                                model_info.append({
                                    'class_name': node.name,
                                    'base_class': base_class_name,
                                    'file': file,
                                    'methods': [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                                })
    return model_info
