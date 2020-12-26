# -*- coding: utf-8; mode: python; mode: flycheck -*-
# pylint: disable=invalid-name,redefined-builtin
# pylint: disable=line-too-long
"""Python package meta informations used by setup.py and other project files.

Single point of source for all xxxx package metadata.  After modifying this
file it is needed to recreate some projet files::

  ./local/py3/bin/python -c "from xxxx.__pkginfo__ import *; print(README)" > README.rst
  ./local/py3/bin/python -c "from xxxx.__pkginfo__ import *; print(requirements_txt)" > requirements.txt

About python packaging see `Python Packaging Authority`_.  Most of the names
here are mapped to ``setup(<name1>=..., <name2>=...)`` arguments in
``setup.py``.  See `Packaging and distributing projects`_ about ``setup(...)``
arguments. If this is all new for you, start with `PyPI Quick and Dirty`_.

Further read:

- pythonwheels_
- setuptools_
- packaging_
- sdist_
- installing_

.. _`Python Packaging Authority`: https://www.pypa.io
.. _`Packaging and distributing projects`: https://packaging.python.org/guides/distributing-packages-using-setuptools/
.. _`PyPI Quick and Dirty`: https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
.. _pythonwheels: https://pythonwheels.com/
.. _setuptools: https://setuptools.readthedocs.io/en/latest/setuptools.html
.. _packaging: https://packaging.python.org/guides/distributing-packages-using-setuptools/#packaging-and-distributing-projects
.. _sdist: https://packaging.python.org/guides/distributing-packages-using-setuptools/#source-distributions
.. _bdist_wheel: https://packaging.python.org/guides/distributing-packages-using-setuptools/#pure-python-wheels
.. _installing: https://packaging.python.org/tutorials/installing-packages/

"""
# pylint: enable=line-too-long

from setuptools import find_packages

package = 'boilerplate'
version = '20200727'
license   = 'GPLv3'
description = 'xxxx lorem ipsum'
copyright = '2020 Markus Heiser'

author = 'Markus Heiser'
author_email = 'markus.heiser@darmarIT.de'

maintainer = 'Markus Heiser'
maintainer_email = 'markus.heiser@darmarIT.de'

url = 'https://github.com/name/boilerplate'
docs = 'https://return42.github.io/boilerplate'
issues = url + '/issues'

authors      = [author, ]

emails       = [author_email, ]
keywords     = 'sphinx extension doc source code comments kernel-doc linux'

maintainers = [maintainer, ]

project_urls = {
    'Documentation'    : docs,
    'Code'             : url,
    'Issue tracker'    : issues,
}

packages = find_packages(exclude=['docs', 'tests'])

# https://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files
package_data = {
#     'xxxx' : [
#         'config.ini',
#         'log.ini',
#         'mime.types',
#     ]
}


# https://docs.python.org/distutils/setupscript.html#installing-additional-files
# https://setuptools.readthedocs.io/en/latest/setuptools.html?highlight=options.data_files#configuring-setup-using-setup-cfg-files
# https://www.scivision.dev/newer-setuptools-needed/
# https://setuptools.readthedocs.io/en/latest/history.html#v40-5-0
data_files = [
#     ('/etc/xxxx', [
#         'xxxx/config.ini',
#         'xxxx/log.ini',
#     ])
#     , ('/usr/share/doc/xxxx', [
#         'README.rst',
#         'LICENSE.txt',
#     ])
]


# https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
python_requires  ='>=3.7'

# https://packaging.python.org/guides/distributing-packages-using-setuptools/#py-modules
py_modules = []

# Since pip v18.1 [PEP508-URL] is supported!
#
# Don't use depricated [dependency_links] any more.  See [git+] for using repos
# as packages.  E.g. 'xxxx's master from github with *all extras* is added to
# the requirements by::
#
#        xxxx @ git+https://github.com/return42/xxxx[devel,test]
#
#  The setup.py 'extra_requires' addressed with [PEP-508 extras], here in the
#  example 'devel' and 'test' requirements also installed.
#
# [PEP-508 URL]      https://www.python.org/dev/peps/pep-0508/
# [PEP-508 extras]   https://www.python.org/dev/peps/pep-0508/#extras
# [git+] https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support
# [requirements.txt] https://pip.pypa.io/en/stable/user_guide/#requirements-files
# [dependency_links] https://python-packaging.readthedocs.io/en/latest/dependencies.html

install_requires = [
    'fspath',
    'tinycss2',
    'requests',
    'sqlalchemy',
]

install_requires_txt = "\n".join(install_requires)

test_requires = [
    'pylint'
    ]

test_requires_txt = "\n".join(test_requires)

develop_requires = [
    'twine',
    # 'wheel'
    'Sphinx<3.0',
    'pallets-sphinx-themes',
    'sphinx-autobuild',
    'sphinx-issues',
    'sphinx-jinja',
    'sphinx-tabs',
    'sphinxcontrib-programoutput',
    'linuxdoc @ git+http://github.com/return42/linuxdoc.git',
    # slide-shows with revaljs
    'sphinxjp.themes.revealjs @ git+https://github.com/return42/sphinxjp.themes.revealjs',
    # https://jedi.readthedocs.io/
    # 'jedi',
    # epc required by emacs: https://tkf.github.io/emacs-jedi
    # 'epc @ git+https://github.com/tkf/python-epc',
    ]


develop_requires_txt = "\n".join(develop_requires)

def get_entry_points():
    """get entry points of the python package"""
    return {
        'console_scripts': [
            'xxxx = xxxx.cli:main' # Main xxxx_ console script
        ]}

# See https://pypi.python.org/pypi?%3Aaction=list_classifiers
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

docstring = """\

.. sidebar::  Info

   - %(package)s (%(version)s)
   - %(copyright)s / %(license)s
   - %(url)s

Nothing special here, only some of my boilerplates

Documentation is available at ./docs or jump to:

  %(docs)s
""" % globals()

# docstring = """
# .. sidebar::  Info
#
#    - %(package)s (%(version)s)
#    - %(copyright)s / %(license)s
#    - %(url)s
#
# The python `xxxx <%(docs)s>`__ package helps .. .  It comes with an API and the
# xxxx command line (see `use <%(docs)s/use.html>`__).
#
# Install
# =======
#
# Install and update using `pip <https://pip.pypa.io/en/stable/quickstart/>`__:
#
# .. code:: bash
#
#    pip install -U %(package)s
# """ % globals()


README = """\
===========
%(package)s
===========
%(docstring)s
""" % globals()

requirements_txt = """# -*- coding: utf-8; mode: conf -*-

# requirements of package %(package)s
# -----------------------------------

%(install_requires_txt)s

# test requires
# -------------

%(test_requires_txt)s

# develop
# -------

%(develop_requires_txt)s
""" % globals()
