# 1. The actual logic
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# 2. The Tests
def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 5) == 5
    print("Subtraction Test Passed!")

# 3. The Execution Block
if __name__ == "__main__":
    try:
        # We must define these above before we call them here!
        test_add_positive_numbers() 
        test_subtract() 
        print("✅ All tests passed!")
    except Exception as e:
        print(f"❌ Error encountered: {e}")
        exit(1)