#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

from typing import Callable, List, Union
from xml.dom import minidom

from svg.path import parse_path
from svg.path.path import Arc, CubicBezier, Linear, Move, Path, QuadraticBezier

__all__ = (
    "Segments",
    "DEFAULT_SCALAR",
    "DEFAULT_BIAS",
    "FLOAT_TO_COMPLEX",
    "get_svg_path_elements",
    "parse_paths",
    "create_path_function",
    "create_path_function_from_file")


Segments = Union[
    Linear, CubicBezier, QuadraticBezier, Arc, Move]

DEFAULT_SCALAR: complex = 1 + 0j
DEFAULT_BIAS: complex = 0 + 0j
FLOAT_TO_COMPLEX = Callable[[float], complex]


def get_svg_path_elements(filename: str) -> List[str]:
    doc = minidom.parse(filename)

    path_strings: List[str] = []

    path: minidom.Element
    for path in doc.getElementsByTagName("path"):
        path_strings.append(path.getAttribute("d"))

    doc.unlink()

    return path_strings


def parse_paths(path_elements: List[str]) -> Path:
    segments: List[Segments] = []

    for string in path_elements:
        segments.extend(parse_path(string))

    path = Path(*segments)

    # pre-calculate and cache all values
    # for the class to work
    path._calc_lengths()

    return path


def create_path_function(
        path: Path, scalar: complex = DEFAULT_SCALAR,
        bias: complex = DEFAULT_BIAS) -> FLOAT_TO_COMPLEX:

    def f(t: float) -> complex:
        return scalar * (path.point(t) + bias)

    return f


def create_path_function_from_file(
        filename: str, scalar: complex = DEFAULT_SCALAR,
        bias: complex = DEFAULT_BIAS) -> FLOAT_TO_COMPLEX:

    return create_path_function(
        parse_paths(get_svg_path_elements(filename)),
        scalar, bias)
