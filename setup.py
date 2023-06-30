#!/usr/bin/env python
"""
xxxx ``setup.py``

Metadata see ``xxxx/__pkginfo__.py``
"""
# pylint: disable=invalid-name

import os
import io
import importlib
from setuptools import setup, find_packages

_dir = os.path.abspath(os.path.dirname(__file__))

SRC    = os.path.join(_dir, 'xxxx')
README = os.path.join(_dir, 'README.rst')
DOCS   = os.path.join(_dir, 'docs')
TESTS  = os.path.join(_dir, 'tests')


def load_source(modname, modpath):
    spec = importlib.util.spec_from_file_location(modname, modpath)
    if not spec:
        raise ValueError("Error loading '%s' module" % modpath)
    module = importlib.util.module_from_spec(spec)
    if not spec.loader:
        raise ValueError("Error loading '%s' module" % modpath)
    spec.loader.exec_module(module)
    return module


def readFile(fname, m='rt', enc='utf-8', nl=None):
    with io.open(fname, mode=m, encoding=enc, newline=nl) as f:
        return f.read()

PKG = load_source('__pkginfo__', os.path.join(SRC, '__pkginfo__.py'))


# https://packaging.python.org/guides/distributing-packages-using-setuptools/#configuring-your-project
setup(
    name               = PKG.package
    , version          = PKG.version
    , description      = PKG.description
    , long_description = PKG.docstring
    , url              = PKG.url

    , author           = PKG.author
    , author_email     = PKG.author_email
    , maintainer       = PKG.maintainer
    , maintainer_email = PKG.maintainer_email

    , license          = PKG.license
    , classifiers      = PKG.classifiers
    , keywords         = PKG.keywords
    , project_urls     = PKG.project_urls

    , packages         = PKG.packages
    , py_modules       = PKG.py_modules

    , install_requires = PKG.install_requires
    , python_requires  = PKG.python_requires

    , package_data     = PKG.package_data
    , data_files       = PKG.data_files
    , entry_points     = PKG.get_entry_points()

    , extras_require   = {
        # usage: pip install .\[develop,test\]
        # - https://pip.pypa.io/en/stable/reference/pip_install/#examples
        # - https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies
        'develop' : PKG.develop_requires
        , 'test'  : PKG.test_requires
    }

)
