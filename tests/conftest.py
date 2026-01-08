"""
Pytest configuration and fixtures.
"""

import sys
from pathlib import Path

import pytest

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def temporary_dir(tmp_path):
    """Provide a temporary directory for tests."""
    return tmp_path
