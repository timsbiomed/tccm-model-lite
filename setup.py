#!/usr/bin/env python
import sys
from setuptools import setup, find_packages
from warnings import warn

if sys.version_info < (3, 7, 0):
    warn(f"Python version 3.7 or later is required for tccm-model.  Current version: {sys.version_info}")
    sys.exit(1)

setup(
    setup_requires=['pbr'],
    packages=find_packages(),
    pbr=True,
)
