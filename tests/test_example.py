"""
Example tests for mypackage.
"""

import pytest

from mypackage import ExampleClass, main_function, utility_function


class TestExampleClass:
    """Test suite for ExampleClass."""

    def test_init(self):
        """Test class initialization."""
        obj = ExampleClass(10)
        assert obj.value == 10

    def test_multiply(self):
        """Test multiplication method."""
        obj = ExampleClass(5)
        assert obj.multiply(3) == 15

    def test_multiply_with_zero(self):
        """Test multiplication with zero."""
        obj = ExampleClass(7)
        assert obj.multiply(0) == 0


class TestFunctions:
    """Test suite for module functions."""

    def test_main_function(self):
        """Test the main function."""
        result = main_function()
        assert isinstance(result, str)
        assert "Hello" in result

    def test_utility_function_with_data(self):
        """Test utility function with data."""
        result = utility_function("test", "default")
        assert result == "test"

    def test_utility_function_with_none(self):
        """Test utility function with None data."""
        result = utility_function(None, "default")
        assert result == "default"


def test_import():
    """Test that the package can be imported."""
    import mypackage

    assert hasattr(mypackage, "__version__")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
