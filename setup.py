#!/usr/bin/env python3
from setuptools import find_packages, setup

test_dependencies = [
        'pytest==6.2.3',
        'pylint==2.9.3',
        'mock==4.0.3',
        'tox==3.24.3'
    ]

extras = {
        'debug': ['ptvsd==4.2.3'],
        'test': test_dependencies,
    }

setup(
    name='plotr-modules',
    version='0.0.1',
    description="Shared Modules for Plotr",
    url='https://github.com/stewartmoreland/plotr-modules',
    include_package_data=True,
    install_requires=[
        'numpy==1.22.3',
        'pandas==1.4.2'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    extras_require=extras,
    tests_require=test_dependencies
)
