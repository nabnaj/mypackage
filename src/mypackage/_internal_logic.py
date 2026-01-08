"""
Internal logic - not intended for direct user access.
This module is considered private API and may change without notice.
"""

# Prefix with underscore to indicate internal use
_INTERNAL_CONSTANT = 42


def _internal_function() -> str:
    """Internal function for package logic.

    Returns:
        Internal message.
    """
    return f"Internal value: {_INTERNAL_CONSTANT}"


def process_internally(data: list) -> list:
    """Process data using internal logic.

    Args:
        data: List of values to process.

    Returns:
        Processed list with internal constant added.
    """
    return [item + _INTERNAL_CONSTANT for item in data]
