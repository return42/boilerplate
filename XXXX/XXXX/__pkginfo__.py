# -*- coding: utf-8; mode: python; mode: flycheck -*-
# pylint: disable=invalid-name,redefined-builtin
"""
python package meta informations used by setup.py

- https://packaging.python.org/guides/distributing-packages-using-setuptools/

"""

package = 'XXXXXX'
version = '20190831.1.post'

copyright = '2019 Markus Heiser'
description = 'Pluginable library ... lorem ipsum ...'
license = 'GPLv2'
keywords = 'fonts TTF OTF WOFF WOFF2  ... lorem ipsum ...'

author = 'Markus Heiser'
author_email = 'markus.heiser@darmarIT.de'
authors = [author, ]

maintainer = 'Markus Heiser'
maintainer_email = 'markus.heiser@darmarIT.de'
maintainers = [maintainer, ]

url = 'https://github.com/return42/XXXXXX'
docs = 'http://return42.github.io/XXXXXX'
issues = 'https://github.com/return42/XXXXXX/issues'

project_urls = {
    # pylint: disable=bad-continuation
    'Documentation'      : docs
    , 'Code'             : url
    , 'Issue tracker'    : issues
}

package_data = {'XXXXXX' : ['cantarell','dejavu']}

python_requires  ='>=3.5'

# Since pip v18.1 [PEP508-URL] is supported!
#
# Don't use depricated [dependency_links] any more.  See [git+] for using repos
# as packages.  E.g. 'XXXXXX's master from github with *all extras* is added to
# the requirements by::
#
#        XXXXXX @ git+https://github.com/return42/XXXXXX[devel,test]
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
    'fspath'
    , 'tinycss2'
    , 'requests'
    , 'sqlalchemy'
    , 'sqlalchemy_schemadisplay @ git+https://github.com/fschulze/sqlalchemy_schemadisplay'
    , 'psycopg2-binary'
]

install_requires_txt = "\n".join(install_requires)

test_requires = [
    'pylint'
    ]

test_requires_txt = "\n".join(test_requires)

develop_requires = [
    'jedi'
    , 'Sphinx'
    , 'sphinx_rtd_theme'
    , 'sphinx-autobuild'
    , 'sphinxcontrib-programoutput'
    , 'pip'
    , 'twine'
]

develop_requires_txt = "\n".join(develop_requires)

requirements_txt = """# -*- coding: utf-8; mode: conf -*-
# ----------------
# install requires
# ----------------

%(install_requires_txt)s

# -------------
# test requires
# -------------

%(test_requires_txt)s

#tox
#pytest
#pytest-cov

# ----------------
# develop requires
# ----------------

%(develop_requires_txt)s

#wheel
#mock

# sphinxjp.themes.revealjs: slide-shows with revaljs
#
#   comment out next lines, if you don't build slide-shows
#
#git+https://github.com/return42/sphinxjp.themes.revealjs
# -e file:../sphinxjp.themes.revealjs#egg=sphinxjp.themes.revealjs

""" % globals()

def get_entry_points():
    """get entry points of the python package"""
    return {
        'console_scripts': [
            'XXXXXX = XXXXXX.cli:main' # Main XXXXXX_ console script
        ]}

# See https://pypi.python.org/pypi?%3Aaction=list_classifiers
classifiers = [
    "Development Status :: 5 - Production/Stable"
    , "Intended Audience :: Developers"
    , "License :: OSI Approved :: GNU General Public License v2 (GPLv2)"
    , "Operating System :: OS Independent"
    , "Programming Language :: Python"
    , "Programming Language :: Python :: 3"
    , "Programming Language :: Python :: Implementation :: CPython"
    , "Programming Language :: Python :: Implementation :: PyPy"
    , "Topic :: Software Development :: Libraries :: Application Frameworks"
    , "Topic :: Software Development :: Libraries :: Python Modules"
]

docstring = """
The python `XXXXXX <%(docs)s>`__ package helps ... lorem ipsum ...

Install
=======

Install and update using `pip <https://pip.pypa.io/en/stable/quickstart/>`__:

.. code-block:: text

   pip install -U XXXXXX


Links
=====

- Documentation:   %(docs)s
- Releases:        https://pypi.org/project/XXXXXX/
- Code:            %(url)s
- Issue tracker:   %(url)s/issues

============ ===============================================
package:     %(package)s (%(version)s)
copyright:   %(copyright)s
e-mail:      %(maintainer_email)s
license:     %(license)s
============ ===============================================

""" % globals()
