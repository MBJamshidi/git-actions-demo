def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b

def test_add_positive_numbers():
    assert add(2, 3) == 5, "Should be 5"

def test_add_zero():
    assert add(5, 0) == 5, "Should be 5"

def test_add_negative_numbers():
    assert add(-1, -1) == -2, "Should be -2"

if __name__ == "__main__":
    # Run all tests
    try:
        test_add_positive_numbers()
        test_add_zero()
        test_add_negative_numbers()
        print("✅ All tests passed successfully!")
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        exit(1) # This tells GitHub Actions that something went wrong!