"""
This module contains the setup script for the Python package. The script uses setuptools
to define the package's metadata, dependencies, and entry points. This script should be
run using the `python setup.py` command.

For more information on using setuptools to define Python packages, see the setuptools
documentation: https://setuptools.pypa.io/en/latest/setuptools.html
"""

from setuptools import setup

setup(
    name="s23openalex",
    version="0.0.1",
    description="bibtex utilities",
    maintainer="Po Chun Chen",
    maintainer_email="pochunc@andrew.cmu.edu",
    license="MIT",
    packages=["s23openalex"],
    scripts=[],
    entry_points={"console_scripts": ["orderA = s23openalex.main:main"]},
    long_description="""A set of bibtex utilities""",
)
