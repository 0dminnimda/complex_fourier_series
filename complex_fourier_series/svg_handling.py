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
        parse_paths(get_svg_path_elements(name)),
        scalar, bias)


if __name__ == "__main__":
    n = 0.5
    scale = 8
    x_off = 0  # pd.scr[0]/16
    y_off = 0  # pd.scr[1]/10
    name = "./icons/" + "pi.svg"

    f = create_path_function_from_file(name)

    # , n, scale=scale, x_off=x_off, y_off=y_off, cent=1)

    #_ = pd.pau()
    # for x,y in path:
    #     pd.circ("white", (x+wid/2, y+hei/2), 2)
    #     pd.upd()
    # _ = pd.pau()

    # for item in segments:
    #     length = item.length()
    #     # lengths.append(length := item.length())
    #     pass
    # step = round(length/freq)
    # for time in range(step):
    #     time/=step
    #     pos = item.point(time)
    #     path.append([(pos.real+x_off)*scale, (pos.imag+y_off)*scale])
