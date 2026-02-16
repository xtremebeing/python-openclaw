"""Tests for openclaw exceptions"""

import pytest
from openclaw.exceptions import OpenClawError, OpenClawConnectionError, OpenClawAuthError


def test_openclaw_error():
    """Test base OpenClawError exception"""
    error = OpenClawError("Test error")
    assert str(error) == "Test error"
    assert isinstance(error, Exception)


def test_openclaw_connection_error():
    """Test OpenClawConnectionError exception"""
    error = OpenClawConnectionError("Connection failed")
    assert str(error) == "Connection failed"
    assert isinstance(error, OpenClawError)
    assert isinstance(error, Exception)


def test_openclaw_auth_error():
    """Test OpenClawAuthError exception"""
    error = OpenClawAuthError("Authentication failed")
    assert str(error) == "Authentication failed"
    assert isinstance(error, OpenClawError)
    assert isinstance(error, Exception)
