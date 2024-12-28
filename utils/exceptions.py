class CodeTestingError(Exception):
    """Base exception for code testing errors"""
    pass

class ValidationError(CodeTestingError):
    """Raised when code validation fails"""
    pass