import ast

def get_base_class_name(base):
    """Get the name of the base class from the AST node."""
    if isinstance(base, ast.Name):
        return base.id
    elif isinstance(base, ast.Attribute):
        return base.attr
    return None
