"""
mypackage - A Python package for amazing things.
"""

__version__ = "0.1.0"
__author__ = "Your Name <your.email@example.com>"

# Import key modules for easier access
from .core import ExampleClass, main_function
from .utils import utility_function

# Define what should be available when using 'from package import *'
__all__ = [
    "main_function",
    "ExampleClass",
    "utility_function",
]
