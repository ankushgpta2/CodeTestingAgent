import io
import inspect
import traceback
from contextlib import redirect_stdout
from typing import Any, Dict
import openai
from models.datatypes import CodeSpec, TestResult
from analyzers.code_analyzer import CodeAnalyzer
from utils.exceptions import TestExecutionError