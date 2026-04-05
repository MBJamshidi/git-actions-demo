def subtract(a, b):
    return a - b

def test_subtract():
    assert subtract(10, 5) == 5
    print("Subtraction Test Passed!")

# Add test_subtract() to your main execution block at the bottom
if __name__ == "__main__":
    try:
        test_add_positive_numbers()
        test_subtract() # New test!
        print("✅ All tests passed!")
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        exit(1)