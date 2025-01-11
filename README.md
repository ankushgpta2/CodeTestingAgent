# Code Testing Agent Framework

## 🚀 Overview
An AI-powered code testing framework that analyzes, tests, and provides feedback on code based on specifications.

## ✨ Key Features
- Static code analysis using AST
- Automatic test case generation
- AI-powered edge case analysis
- Comprehensive test execution
- Detailed feedback and reporting

### 🤖 Supported Language Models

| Model     | Provider     | Support Level     | Capabilities     |
|--------------|--------------|--------------|--------------|
| GPT-4 | OpenAI | Full | Advanced analysis, comprehensive feedback |
| GPT-3.5 Turbo | OpenAI | Basic | Standard analysis, limited depth |
| Claude 3 Opus | Anthropic | Experimental | Advanced reasoning, nuanced feedback |

## 💻 Installation

### Install from PyPI
```bash
pip install code-testing-agent
```

### Or install from source
```bash
git clone https://github.com/yourusername/code-testing-agent.git
cd code-testing-agent
pip install -e .
```

## 🔧 Configuration

### 🔑 API Key Management

#### Environment Variables
```python
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = 'your-openai-api-key'
```

#### Direct Configuration
```python
from code_testing_agent import CodeTester

# Initialize with API key
tester = CodeTester(llm_api_key='your-api-key')
```

## 🔬 Detailed Component Breakdown

### 1. CodeSpec (Specification Model)
```python
CodeSpec(
    description: str,  # Human-readable description of the code
    expected_inputs: Dict[str, type],  # Input type constraints
    expected_outputs: Dict[str, type],  # Output type constraints
    example_test_cases: List[Dict[str, Any]],  # Predefined test cases
    constraints: Optional[List[str]] = None  # Additional code constraints
)
```

#### Example
```python 
spec = CodeSpec(
    description="Calculate average of a list of numbers",
    expected_inputs={"numbers": list},
    expected_outputs={"result": float},
    example_test_cases=[
        {
            "inputs": {"numbers": [1, 2, 3, 4, 5]},
            "expected": 3.0
        }
    ],
    constraints=[
        "Input list must contain only numbers",
        "Handles empty list by returning 0"
    ]
)
```

### 2. 🕵️ Advanced Analysis Techniques

#### Static Code Analysis

- Abstract Syntax Tree (AST) parsing
- Syntax structure evaluation
- Potential issue detection
- Code complexity assessment

#### Potential Detected Issues

- Mutable default arguments
- Infinite loops
- Redundant comparisons
- Exception handling anti-patterns

## 🚀 Advanced Usage

### Custom Model Configuration
```python
from code_testing_agent import CodeTester
```

```python
# Configure with custom OpenAI model
tester = CodeTester(
    llm_api_key='your-key',
    model='gpt-4',  # Specify model
    temperature=0.7,  # Adjust creativity
    max_tokens=500   # Limit response length
)
```

### Extending Analysis
```python
from code_testing_agent.analyzers import CodeAnalyzer

class CustomCodeAnalyzer(CodeAnalyzer):
    def additional_checks(self, tree: ast.AST):
        # Add custom static analysis rules
        pass
```

## 🛠 Error Handling

### Custom Exceptions

```CodeTestingError```: Base exception
```ValidationError```: Code validation failures
```TestExecutionError```: Test runtime errors

```python
try:
    result = tester.test_code(code, spec)
except ValidationError as e:
    print(f"Code validation failed: {e}")
except TestExecutionError as e:
    print(f"Test execution error: {e}")
```

## 📊 Performance Considerations

- Caching analysis results
- Configurable recursion limits
- Timeout mechanisms for long-running tests
- Selective test case execution


## 🚦 Future Roadmap
- Multi-language support
- More advanced AI models
- Enhanced test case generation
- Performance profiling
- Integration with CI/CD pipelines