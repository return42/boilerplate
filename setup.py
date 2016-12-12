#!/usr/bin/env python
# -*- coding: utf-8; mode: python -*-

from setuptools import setup, find_packages
import XXXX

install_requires = [
    "fspath"
    , "six" ]

setup(
    name               = "XXXX"
    , version          = XXXX.__version__
    , description      = XXXX.__description__
    , long_description = XXXX.__doc__
    , url              = XXXX.__url__
    , author           = "Markus Heiser"
    , author_email     = "markus.heiser@darmarIT.de"
    , license          = XXXX.__license__
    , keywords         = "path-names development"
    , packages         = find_packages(exclude=['docs', 'tests'])
    , install_requires = install_requires

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    , classifiers = [
        "Development Status :: 5 - Production/Stable"
        , "Intended Audience :: Developers"
        , "License :: OSI Approved :: GNU General Public License v2 (GPLv2)"
        , "Operating System :: OS Independent"
        , "Programming Language :: Python"
        , "Programming Language :: Python :: 2"
        , "Programming Language :: Python :: 3"
        , "Topic :: Utilities"
        , "Topic :: Software Development :: Libraries"
        , "Topic :: System :: Filesystems" ]
)
