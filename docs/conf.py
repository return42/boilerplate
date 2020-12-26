# -*- coding: utf-8 -*-
#
# Sphinx documentation build configuration file

import re
import xxxx
import xxxx.__pkginfo__ as PKG
import sys, os

from pallets_sphinx_themes import ProjectLink

sys.path.append(os.path.abspath('../utils/site-python'))
from sphinx_build_tools import load_sphinx_config

project   = 'xxxx'
copyright = xxxx.__copyright__
version   = xxxx.__version__
release   = xxxx.__version__
show_authors = True

DOC_URL    = PKG.docs
GIT_URL    = PKG.url
GIT_BRANCH = 'master'

source_suffix       = '.rst'
show_authors        = True
master_doc          = 'index'
templates_path      = ['_templates']
exclude_patterns    = ['_build', 'slides', 'index-autodoc.rst']
todo_include_todos  = True
highlight_language = 'none'

extensions = [
    'sphinx.ext.imgmath'
    , 'sphinx.ext.autodoc'
    , 'sphinx.ext.extlinks'
    #, 'sphinx.ext.autosummary'
    #, 'sphinx.ext.doctest'
    , 'sphinx.ext.todo'
    , 'sphinx.ext.coverage'
    #, 'sphinx.ext.pngmath'
    #, 'sphinx.ext.mathjax'
    , 'sphinx.ext.viewcode'
    , 'sphinx.ext.intersphinx'
    , 'linuxdoc.rstFlatTable'    # Implementation of the 'flat-table' reST-directive.
    , 'linuxdoc.rstKernelDoc'    # Implementation of the 'kernel-doc' reST-directive.
    , 'linuxdoc.kernel_include'  # Implementation of the 'kernel-include' reST-directive.
    , 'linuxdoc.manKernelDoc'    # Implementation of the 'kernel-doc-man' builder
    , 'linuxdoc.cdomain'         # Replacement for the sphinx c-domain.
    , 'linuxdoc.kfigure'         # Sphinx extension which implements scalable image handling.
    , 'sphinx_tabs.tabs'         # https://github.com/djungelorm/sphinx-tabs
    , 'pallets_sphinx_themes'
    , 'sphinxcontrib.programoutput'  # https://github.com/NextThought/sphinxcontrib-programoutput

]

# usage:    :ref:`comparison manual <python:comparisons>`
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "flask": ("https://flask.palletsprojects.com/", None),
    # "werkzeug": ("https://werkzeug.palletsprojects.com/", None),
    "jinja": ("https://jinja.palletsprojects.com/", None),
    "linuxdoc" : ("https://return42.github.io/linuxdoc/", None),
    "sphinx" : ("https://www.sphinx-doc.org/en/master/", None),
}


# usage::   lorem :patch:`f373169` ipsum
extlinks = {}
extlinks['wiki']   = (GIT_URL + '/wiki/%s', ' ')
extlinks['pull']   = (GIT_URL + '/pull/%s', 'PR ')
extlinks['origin'] = (GIT_URL + '/blob/' + GIT_BRANCH + '/%s', 'git://')
extlinks['patch']  = (GIT_URL + '/commit/%s', '#')
extlinks['docs']   = (DOC_URL + '/%s', 'docs: ')
extlinks['pypi'] = ('https://pypi.org/project/%s', 'PyPi: ')
extlinks['man'] = ('https://manpages.debian.org/jump?q=%s', '')
#extlinks['role'] = (
#    'https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-%s', '')
extlinks['duref'] = (
    'http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#%s', '')
extlinks['durole'] = (
    'http://docutils.sourceforge.net/docs/ref/rst/roles.html#%s', '')
extlinks['dudir'] =  (
    'http://docutils.sourceforge.net/docs/ref/rst/directives.html#%s', '')
extlinks['ctan'] =  (
    'https://ctan.org/pkg/%s', 'CTAN: ')

# sphinx.ext.imgmath setup
html_math_renderer = 'imgmath'
imgmath_image_format = 'svg'
imgmath_font_size = 14
# sphinx.ext.imgmath setup END

html_search_language = 'en'

sys.path.append(os.path.abspath('_themes'))
html_theme           = "custom"
html_logo            = 'darmarIT_logo_128.png'
html_theme_path      = ['_themes']

html_theme_options = {"index_sidebar_logo": True}
html_context = {
    "project_links": [
        ProjectLink("Slide Collection", DOC_URL + '/slides/index.html'),
        #ProjectLink("Home", DOC_URL),
        ProjectLink("Source", GIT_URL),
        ProjectLink("API", DOC_URL+ '/xxxx-api/xxxx.html'),

    ]
}
html_sidebars = {
    "**": ["project.html", "relations.html", "localtoc.html", "searchbox.html"],
}
singlehtml_sidebars = {"index": ["project.html", "localtoc.html"]}

# ------------------------------------------------------------------------------
# Since loadConfig overwrites settings from the global namespace, it has to be
# the last statement in the conf.py file
# ------------------------------------------------------------------------------
load_sphinx_config(globals())
