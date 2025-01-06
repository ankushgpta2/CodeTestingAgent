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
    
    def test_code(self, code_str: str, spec: CodeSpec) -> TestResult:
        """Test code against given specifications"""
        issues = self.analyzer.analyze_code(code_str)
        if issues:
            return TestResult(
                passed=False,
                error_message="Static analysis found potential issues",
                feedback="\n".join(issues)
            )
        
        test_env: Dict[str, Any] = {}
        output_buffer = io.StringIO()

        try:
            with redirect_stdout(output_buffer):
                exec(code_str, test_env)

            self._run_test_cases(test_env, spec)
            edge_case_feedback = self._get_ai_edge_case_feedback(code_str, spec)

            return TestResult(
                passed=True,
                output=output_buffer.getvalue(),
                feedback=edge_case_feedback
            )

        except Exception as e:
            return TestResult(
                passed=False,
                error_message=str(e),
                stack_trace=traceback.format_exc(),
                output=output_buffer.getvalue()
            )
    
    def _run_test_cases(self, test_env: Dict[str, Any], spec: CodeSpec) -> None:
        """Run specified test cases"""
        main_func = None
        for item in test_env.values():
            if inspect.isfunction(item):
                main_func = item
                break
        
        for test_case in spec.example_test_cases:
            inputs = test_case["inputs"]
            expected_output = test_case["expected"]
            
            actual_output = main_func(**inputs)

            if not main_func:
                raise TestExecutionError("No function found in provided code")
        
            if actual_output != expected_output:
                raise TestExecutionError(
                    f"Test case failed: Expected {expected_output}, got {actual_output}"
                )
    
    def _get_ai_edge_case_feedback(self, code_str: str, spec: CodeSpec) -> str:
        """Use LLM to analyze potential edge cases and provide feedback"""
        prompt = f"""
        Analyze this code and specification for potential edge cases and improvements:
        
        Code:
        {code_str}
        
        Specification:
        {spec.description}

        Expected inputs: {spec.expected_inputs}
        Expected outputs: {spec.expected_outputs}

        Please identify:
        1. Potential edge cases not covered
        2. Input validation improvements
        3. Error handling suggestions
        4. Performance considerations
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )