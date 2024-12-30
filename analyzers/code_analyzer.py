import ast
from typing import List
from ..utils.exceptions import ValidationError

class CodeAnalyzer:
    """Analyzes code structure and potential issues"""
    
    def __init__(self):
        self.issues: List[str] = []
    
    def check_syntax(self, tree: ast.AST) -> None:
        """Check basic syntax structures"""
        for node in ast.walk(tree):
            if isinstance(node, ast.ExceptHandler) and node.type is None:
                self.issues.append("Warning: Using bare 'except' clause - consider catching specific exceptions")
            
            if isinstance(node, ast.FunctionDef):
                for default in node.args.defaults:
                    if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                        self.issues.append(f"Warning: Mutable default argument in function {node.name}")