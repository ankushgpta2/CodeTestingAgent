import sys
from typing import Any, Dict, List
from ..models.datatypes import CodeSpec


class TestGenerator:
    """Generates test cases based on specifications"""

    def generate_test_cases(self, spec: CodeSpec) -> List[Dict[str, Any]]:
        """Generate comprehensive test cases"""
        test_cases = []
        test_cases.extend(spec.example_test_cases)
        edge_cases = self._generate_edge_cases(spec)

    def _generate_edge_cases(self, spec: CodeSpec) -> List[Dict[str, Any]]:
        """Generate edge cases based on input types"""
        edge_cases = []

        for param_name, param_type in spec.expected_inputs.items():
            if param_type == int:
                edge_cases.extend([
                    {"inputs": {param_name: 0}, "expected": None},
                    {"inputs": {param_name: -1}, "expected": None},
                    {"inputs": {param_name: sys.maxsize}, "expected": None}
                ])
            elif param_type == str:
                edge_cases.extend([
                    {"inputs": {param_name: ""}, "expected": None},
                    {"inputs": {param_name: " "}, "expected": None},
                    {"inputs": {param_name: "a" * 1000}, "expected": None}
                ])
        
        return edge_cases