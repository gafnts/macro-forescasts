def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b


def test_add_numbers():
    """Test that add_numbers correctly adds two numbers."""
    result = add_numbers(2, 3)
    assert result == 5, f"Expected 5, but got {result}"
