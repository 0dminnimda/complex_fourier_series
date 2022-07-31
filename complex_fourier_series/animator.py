#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

import os
from typing import List, Optional, Tuple, Union

import pygame as pg
from pygame.math import Vector2

from .series import Series
from .svg_handling import FLOAT_TO_COMPLEX, create_path_function_from_file

__all__ = (
    "BLACK",
    "VECTOR_COLOR",
    "VECTOR_WIDTH",
    "PATH_COLOR",
    "PATH_WIDTH",
    "main_loop",
    "draw",
    "draw_arrow",
    "draw_path",
    "complex_to_tuple")

BLACK = (0, 0, 0)
VECTOR_COLOR = (255, 0, 0)
VECTOR_WIDTH = 1
PATH_COLOR = (0, 255, 0)
PATH_WIDTH = 1


def main_loop(size: Tuple[int, int], path_func: FLOAT_TO_COMPLEX,
              quantity: int, time_divider: Union[int, float],
              save: Optional[str] = None):
    display = pg.display.set_mode(size)

    series: Series = Series()
    series.create_formulas(quantity, path_func)

    time: int = 0

    path: List[Vector2] = []

    offset: complex = complex(*size) / 2

    if save is not None:
        folder = f"{save}/q{quantity}"
        save = folder + "/screenshot-{time}.jpg"

        if not os.path.exists(folder):
            os.makedirs(folder)

    result = False
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
                result = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    done = True
                    result = True

        display.fill(BLACK)

        draw(display, series, offset, time/time_divider, path)

        if save is not None:
            pg.image.save(display, save.format(time=time))

        pg.display.flip()

        time += 1

        if save is not None and time == int(time_divider):
            done = True  # we need only one cycle at most

        if time == int(2 * time_divider):
            time = 0
            del path[:int(time_divider)]

    return result


def draw(display: pg.surface.Surface, series: Series, offset: complex,
         time: float, path: List[Vector2]) -> None:

    values: List[complex] = series.evaluate_all(time)

    current_value: complex = 0j

    for value in values:
        new_value: complex = current_value + value
        draw_arrow(display,
                   current_value + offset,
                   new_value + offset)
        current_value = new_value

    path.append(Vector2(
        complex_to_tuple(current_value + offset)))

    draw_path(display, path)


def draw_arrow(
    display: pg.surface.Surface,
    from_val: complex,
    to_val: complex,
    end_fraction: float = 0.3,
) -> None:

    direction = to_val - from_val

    tip = direction * end_fraction
    body = to_val - tip

    pg.draw.line(
        display,
        VECTOR_COLOR,
        complex_to_tuple(from_val),
        complex_to_tuple(body),
        VECTOR_WIDTH,
    )

    points = [body + rotate90(tip) / 3, body - rotate90(tip) / 3, to_val]

    pg.draw.polygon(
        display, VECTOR_COLOR, [complex_to_tuple(i) for i in points], VECTOR_WIDTH
    )


def rotate90(num: complex) -> complex:
    return 1j * num.real - num.imag


def draw_path(display: pg.surface.Surface,
              path: List[Vector2]) -> None:

    if len(path) < 2:
        return

    pg.draw.aalines(display, PATH_COLOR, False, path)  # PATH_WIDTH, 


def complex_to_tuple(value: complex) -> Tuple[float, float]:
    return ((value.real), (value.imag))
