# Code Testing Agent Framework

## Overview
An AI-powered code testing framework that analyzes, tests, and provides feedback on code based on specifications.

## Features
- Static code analysis using AST
- Automatic test case generation
- AI-powered edge case analysis
- Comprehensive test execution
- Detailed feedback and reporting

## Installation

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

## Configuration

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