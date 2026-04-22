import pytest

from src.calculator import add, divide, multiply, subtract


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_mixed_signs(self):
        assert add(-5, 10) == 5

    def test_floats(self):
        assert add(1.5, 2.5) == 4.0

    def test_zero(self):
        assert add(0, 0) == 0


class TestSubtract:
    def test_positive_numbers(self):
        assert subtract(10, 5) == 5

    def test_negative_result(self):
        assert subtract(3, 10) == -7

    def test_zero(self):
        assert subtract(5, 5) == 0


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(100, 0) == 0

    def test_negative_numbers(self):
        assert multiply(-2, -3) == 6

    def test_floats(self):
        assert multiply(2.5, 4) == 10.0


class TestDivide:
    def test_positive_numbers(self):
        assert divide(10, 2) == 5

    def test_float_result(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
