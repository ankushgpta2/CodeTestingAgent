import ast
from typing import List
from ..utils.exceptions import ValidationError

class CodeAnalyzer:
    """Analyzes code structure and potential issues"""
    
    def __init__(self):
        self.issues: List[str] = []
    
    