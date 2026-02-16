"""Example usage of python-openclaw"""

from openclaw import (
    OpenClawClient,
    OpenClawError,
    OpenClawConnectionError,
    OpenClawAuthError,
)


def main():
    """Main example function"""

    # Example 1: Basic usage
    print("Example 1: Basic client usage")
    client = OpenClawClient(
        base_url="https://api.openclaw.example.com",
        api_key="your-api-key-here",
        timeout=30,
    )

    try:
        # GET request
        response = client.get("/endpoint")
        print(f"GET Response: {response}")

        # POST request
        data = {"key": "value", "name": "example"}
        response = client.post("/endpoint", json=data)
        print(f"POST Response: {response}")

    except OpenClawAuthError as e:
        print(f"Authentication error: {e}")
    except OpenClawConnectionError as e:
        print(f"Connection error: {e}")
    except OpenClawError as e:
        print(f"General error: {e}")
    finally:
        client.close()

    # Example 2: Using context manager
    print("\nExample 2: Using context manager")
    try:
        with OpenClawClient(base_url="https://api.openclaw.example.com") as client:
            response = client.get("/endpoint", params={"filter": "active"})
            print(f"Response: {response}")
    except OpenClawError as e:
        print(f"Error occurred: {e}")

    # Example 3: Different HTTP methods
    print("\nExample 3: Different HTTP methods")
    with OpenClawClient(base_url="https://api.openclaw.example.com") as client:
        try:
            # GET with query parameters
            get_response = client.get("/users", params={"page": 1, "limit": 10})
            print(f"GET with params: {get_response}")

            # POST with JSON data
            post_response = client.post(
                "/users", json={"name": "John", "email": "john@example.com"}
            )
            print(f"POST response: {post_response}")

            # PUT to update
            put_response = client.put("/users/1", json={"name": "John Updated"})
            print(f"PUT response: {put_response}")

            # DELETE
            delete_response = client.delete("/users/1")
            print(f"DELETE response: {delete_response}")

        except OpenClawError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    print("Python OpenClaw Library - Example Usage")
    print("=" * 50)
    print("\nNote: This example uses placeholder URLs.")
    print("Replace with your actual OpenClaw API endpoints.\n")
    print("=" * 50)

    # Uncomment the line below to run the examples
    # main()

    print("\nTo run this example with a real API:")
    print("1. Replace the base_url with your actual OpenClaw API URL")
    print("2. Add your API key if required")
    print("3. Uncomment the main() call above")
