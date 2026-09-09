import pytest
from calculator import add, multiply


class TestAdd:
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-2, -3) == -5

    def test_add_mixed_signs(self):
        """Test adding numbers with mixed signs."""
        assert add(5, -3) == 2


class TestMultiply:
    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        assert multiply(4, 5) == 20

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-3, -4) == 12

    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(7, 0) == 0
