"""
Core functionality for the package.
"""


class ExampleClass:
    """An example class demonstrating best practices."""

    def __init__(self, value: int):
        """Initialize the class.

        Args:
            value: An integer value.
        """
        self.value = value

    def multiply(self, factor: int) -> int:
        """Multiply the value by a factor.

        Args:
            factor: Multiplication factor.

        Returns:
            The multiplied value.
        """
        return self.value * factor


def main_function() -> str:
    """Main function of the package.

    Returns:
        A greeting message.
    """
    print("Executing main function...")
    return "Hello from the package!"
