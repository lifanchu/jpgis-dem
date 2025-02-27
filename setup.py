#!/usr/bin/python
# coding: utf8


import re


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


with open("jpgisdem/__init__.py", "r") as f:
    version = re.search(r'^__version__ = "([\d\.]+)"', f.read(), re.MULTILINE).group(1)


if not version:
    raise RuntimeError("Cannot find version information")


with open("README.md") as f:
    readme = f.read()

setup(
    name="jpgis-dem",
    version=version,
    packages=find_packages(),
    description="Convert JPGIS .xml DEM files to geotiffs.",
    long_description=readme,
    long_description_content_type='text/markdown',
    url="https://github.com/lifanchu/jpgis-dem",
    download_url="https://github.com/lifanchu/jpgis-dem",
    author="Andrew Nisbet",
    author_email="andrew@gpxz.io",
    license="The MIT License",
    package_data={"": ["LICENSE", "README.md"]},
    py_modules=["jpgisdem"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "jpgis-dem = jpgisdem:cli",
        ],
    },
    keywords="elevation",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: GIS",
    ],
)
