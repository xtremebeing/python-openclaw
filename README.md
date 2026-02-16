# python-openclaw

Python Library for accessing OpenClaw

[![PyPI version](https://badge.fury.io/py/python-openclaw.svg)](https://badge.fury.io/py/python-openclaw)
[![Python Version](https://img.shields.io/pypi/pyversions/python-openclaw.svg)](https://pypi.org/project/python-openclaw/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation

Install from PyPI:

```bash
pip install python-openclaw
```

Or install from source:

```bash
git clone https://github.com/xtremebeing/python-openclaw.git
cd python-openclaw
pip install -e .
```

## Quick Start

```python
from openclaw import OpenClawClient

# Create a client instance
client = OpenClawClient(
    base_url="https://api.openclaw.example.com",
    api_key="your-api-key-here"  # Optional
)

# Make a GET request
response = client.get("/endpoint")
print(response)

# Make a POST request
data = {"key": "value"}
response = client.post("/endpoint", json=data)
print(response)

# Use as a context manager (automatically closes session)
with OpenClawClient(base_url="https://api.openclaw.example.com") as client:
    response = client.get("/endpoint")
    print(response)
```

## Features

- 🚀 Simple and intuitive API
- 🔐 Authentication support (API key/Bearer token)
- 📦 Full REST API support (GET, POST, PUT, DELETE)
- 🛡️ Comprehensive error handling
- 🔄 Session management with context manager support
- ⚡ Type hints for better IDE support
- 🧪 Fully tested

## API Reference

### OpenClawClient

The main client class for interacting with OpenClaw API.

**Parameters:**
- `base_url` (str): Base URL for the OpenClaw API
- `api_key` (str, optional): API key for authentication
- `timeout` (int, optional): Request timeout in seconds (default: 30)

**Methods:**

#### `get(endpoint, params=None)`
Make a GET request to the API.

**Parameters:**
- `endpoint` (str): API endpoint path
- `params` (dict, optional): Query parameters

**Returns:** dict - JSON response

#### `post(endpoint, data=None, json=None)`
Make a POST request to the API.

**Parameters:**
- `endpoint` (str): API endpoint path
- `data` (dict, optional): Form data
- `json` (dict, optional): JSON data

**Returns:** dict - JSON response

#### `put(endpoint, data=None, json=None)`
Make a PUT request to the API.

**Parameters:**
- `endpoint` (str): API endpoint path
- `data` (dict, optional): Form data
- `json` (dict, optional): JSON data

**Returns:** dict - JSON response

#### `delete(endpoint)`
Make a DELETE request to the API.

**Parameters:**
- `endpoint` (str): API endpoint path

**Returns:** dict - JSON response

## Exception Handling

The library provides custom exceptions for better error handling:

```python
from openclaw import OpenClawClient, OpenClawError, OpenClawConnectionError, OpenClawAuthError

try:
    client = OpenClawClient(base_url="https://api.openclaw.example.com")
    response = client.get("/endpoint")
except OpenClawAuthError as e:
    print(f"Authentication error: {e}")
except OpenClawConnectionError as e:
    print(f"Connection error: {e}")
except OpenClawError as e:
    print(f"General error: {e}")
```

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/xtremebeing/python-openclaw.git
cd python-openclaw

# Install development dependencies
pip install -e .[dev]
```

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
# Format code
black openclaw

# Check formatting
black --check openclaw
```

### Linting

```bash
flake8 openclaw
```

### Type Checking

```bash
mypy openclaw
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues, questions, or contributions, please visit the [GitHub repository](https://github.com/xtremebeing/python-openclaw)
