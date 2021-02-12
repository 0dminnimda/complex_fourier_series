#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

from complex_fourier_series import __version__, __name__, __author__
from setuptools import find_packages, setup


with open("README.md", "r") as file:
    long_description = file.read()

with open("requirements.txt", "r") as file:
    requirements = [line.strip() for line in file]

setup(
    name=__name__,
    version=__version__,
    description="Complex fourier series visualisation. "
                "Inspired by youtu.be/r6sGWTCMz2k",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    author_email="0dminnimda.contact@gmail.com",
    packages=find_packages(),
    license="MIT",
    install_requires=requirements,
    python_requires="~=3.8",
)
