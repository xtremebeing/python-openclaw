"""
Exception classes for python-openclaw
"""


class OpenClawError(Exception):
    """Base exception for all OpenClaw errors"""

    pass


class OpenClawConnectionError(OpenClawError):
    """Raised when there's a connection error to OpenClaw"""

    pass


class OpenClawAuthError(OpenClawError):
    """Raised when there's an authentication error"""

    pass
