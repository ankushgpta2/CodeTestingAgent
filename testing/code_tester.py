import io
import inspect
import traceback
from contextlib import redirect_stdout
from typing import Any, Dict
import openai
from ..models.datatypes import CodeSpec, TestResult
from ..analyzers.code_analyzer import CodeAnalyzer
from ..utils.exceptions import TestExecutionError


class CodeTester:
    """Runs and tests code against specifications"""
    
    def __init__(self, llm_api_key: str):
        self.analyzer = CodeAnalyzer()
        openai.api_key = llm_api_key
    
    def test_code(self, code_str, spec) -> TestResult:
        """Test code against given specifications"""
        issues = self.analyzer.analyze_code(code_str)
        if issues:
            return TestResult(
                passed=False,
                error_message="Static analysis found potential issues",
                feedback="\n".join(issues)
            )
        