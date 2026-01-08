"""
Utility functions for the package.
"""

import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)


def setup_logging(level: int = logging.INFO) -> None:
    """Set up basic logging configuration.

    Args:
        level: Logging level (default: logging.INFO).
    """
    logging.basicConfig(
        level=level, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )


def utility_function(data: Any, default: Optional[Any] = None) -> Any:
    """A utility function that processes data.

    Args:
        data: Input data to process.
        default: Default value if data is None.

    Returns:
        Processed data or default value.
    """
    if data is None:
        logger.warning("Data is None, returning default value")
        return default

    # Process data here
    return data


def safe_divide(a: float, b: float) -> float:
    """Safely divide two numbers.

    Args:
        a: Numerator.
        b: Denominator.

    Returns:
        Division result.

    Raises:
        ValueError: If denominator is zero.
    """
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b
