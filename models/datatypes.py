from dataclasses import dataclass
from typing import Any, Dict, List, Optional

@dataclass
class CodeSpec:
    """Specification for code testing"""
    description: str
    expected_inputs: Dict[str, type]
    expected_outputs: Dict[str, type]
    example_test_cases: List[Dict[str, Any]]
    constraints: Optional[List[str]] = None
