"""
OpenClaw client for interacting with OpenClaw services
"""

from typing import Optional, Dict, Any
import requests
from .exceptions import OpenClawConnectionError, OpenClawAuthError, OpenClawError


class OpenClawClient:
    """
    Client for interacting with OpenClaw API
    
    Args:
        base_url: Base URL for the OpenClaw API
        api_key: Optional API key for authentication
        timeout: Request timeout in seconds (default: 30)
    
    Example:
        >>> client = OpenClawClient(base_url="https://api.openclaw.example.com")
        >>> response = client.get("/endpoint")
    """
    
    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        timeout: int = 30
    ):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.Session()
        
        if api_key:
            self.session.headers.update({
                'Authorization': f'Bearer {api_key}'
            })
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        **kwargs
    ) -> requests.Response:
        """
        Make an HTTP request to the OpenClaw API
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            endpoint: API endpoint path
            **kwargs: Additional arguments to pass to requests
        
        Returns:
            Response object
            
        Raises:
            OpenClawConnectionError: If there's a connection error
            OpenClawAuthError: If there's an authentication error
            OpenClawError: For other API errors
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                timeout=self.timeout,
                **kwargs
            )
            
            if response.status_code == 401:
                raise OpenClawAuthError("Authentication failed")
            elif response.status_code == 403:
                raise OpenClawAuthError("Access forbidden")
            
            response.raise_for_status()
            return response
            
        except requests.exceptions.ConnectionError as e:
            raise OpenClawConnectionError(f"Failed to connect to {url}") from e
        except requests.exceptions.Timeout as e:
            raise OpenClawConnectionError(f"Request timeout for {url}") from e
        except OpenClawAuthError:
            raise
        except requests.exceptions.RequestException as e:
            raise OpenClawError(f"Request failed: {str(e)}") from e
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make a GET request
        
        Args:
            endpoint: API endpoint path
            params: Query parameters
            
        Returns:
            JSON response as dictionary
        """
        response = self._make_request('GET', endpoint, params=params)
        return response.json() if response.content else {}
    
    def post(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make a POST request
        
        Args:
            endpoint: API endpoint path
            data: Form data
            json: JSON data
            
        Returns:
            JSON response as dictionary
        """
        response = self._make_request('POST', endpoint, data=data, json=json)
        return response.json() if response.content else {}
    
    def put(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make a PUT request
        
        Args:
            endpoint: API endpoint path
            data: Form data
            json: JSON data
            
        Returns:
            JSON response as dictionary
        """
        response = self._make_request('PUT', endpoint, data=data, json=json)
        return response.json() if response.content else {}
    
    def delete(self, endpoint: str) -> Dict[str, Any]:
        """
        Make a DELETE request
        
        Args:
            endpoint: API endpoint path
            
        Returns:
            JSON response as dictionary
        """
        response = self._make_request('DELETE', endpoint)
        return response.json() if response.content else {}
    
    def close(self):
        """Close the session"""
        self.session.close()
    
    def __enter__(self):
        """Context manager entry"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()
