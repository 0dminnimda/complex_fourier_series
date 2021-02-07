#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

from .animator import main_loop
from .svg_handling import create_path_function_from_file

__all__ = (
    "main_loop",
    "create_path_function_from_file",
    "__name__",
    "__author__",
    "__version__")


__name__ = "complex_fourier_series"
__author__ = "0dminnimda"
__version__ = "0.1.0"
