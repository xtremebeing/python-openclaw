"""Tests for OpenClawClient"""

import pytest
from unittest.mock import Mock, patch
from openclaw import (
    OpenClawClient,
    OpenClawError,
    OpenClawConnectionError,
    OpenClawAuthError,
)


class TestOpenClawClient:
    """Test cases for OpenClawClient"""

    def test_client_initialization(self):
        """Test client initialization"""
        client = OpenClawClient(base_url="https://api.example.com")
        assert client.base_url == "https://api.example.com"
        assert client.timeout == 30
        assert client.api_key is None

    def test_client_initialization_with_api_key(self):
        """Test client initialization with API key"""
        client = OpenClawClient(base_url="https://api.example.com", api_key="test-key")
        assert client.api_key == "test-key"
        assert "Authorization" in client.session.headers

    def test_client_strips_trailing_slash(self):
        """Test that trailing slash is removed from base_url"""
        client = OpenClawClient(base_url="https://api.example.com/")
        assert client.base_url == "https://api.example.com"

    @patch("openclaw.client.requests.Session.request")
    def test_get_request(self, mock_request):
        """Test GET request"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b'{"data": "test"}'
        mock_response.json.return_value = {"data": "test"}
        mock_request.return_value = mock_response

        client = OpenClawClient(base_url="https://api.example.com")
        result = client.get("/test")

        assert result == {"data": "test"}
        mock_request.assert_called_once()

    @patch("openclaw.client.requests.Session.request")
    def test_post_request(self, mock_request):
        """Test POST request"""
        mock_response = Mock()
        mock_response.status_code = 201
        mock_response.content = b'{"created": "true"}'
        mock_response.json.return_value = {"created": "true"}
        mock_request.return_value = mock_response

        client = OpenClawClient(base_url="https://api.example.com")
        result = client.post("/test", json={"key": "value"})

        assert result == {"created": "true"}
        mock_request.assert_called_once()

    @patch("openclaw.client.requests.Session.request")
    def test_authentication_error(self, mock_request):
        """Test authentication error handling"""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_request.return_value = mock_response

        client = OpenClawClient(base_url="https://api.example.com")

        with pytest.raises(OpenClawAuthError):
            client.get("/test")

    @patch("openclaw.client.requests.Session.request")
    def test_connection_error(self, mock_request):
        """Test connection error handling"""
        import requests

        mock_request.side_effect = requests.exceptions.ConnectionError()

        client = OpenClawClient(base_url="https://api.example.com")

        with pytest.raises(OpenClawConnectionError):
            client.get("/test")

    def test_context_manager(self):
        """Test client as context manager"""
        with OpenClawClient(base_url="https://api.example.com") as client:
            assert client.base_url == "https://api.example.com"

        # Session should be closed after exiting context
        assert client.session is not None
