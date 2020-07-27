# -*- coding: utf-8 -*-
#
# Sphinx documentation build configuration file

import re
import XXXX
import sys, os
sys.path.append(os.path.abspath('../utils/site-python'))
from sphinx_build_tools import load_sphinx_config

project   = 'XXXX'
copyright = XXXX.__copyright__
version   = XXXX.__version__
release   = XXXX.__version__
show_authors = True

source_suffix       = '.rst'
show_authors        = True
master_doc          = 'index'
templates_path      = ['_templates']
exclude_patterns    = ['_build', 'slides']
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
    , 'pallets_sphinx_themes',
]

intersphinx_mapping = {}
# usage:    :ref:`comparison manual <python:comparisons>`
intersphinx_mapping['python']  = ('https://docs.python.org/', None)

extlinks = {}
# usage:    :cdb-doc:`admin/platform/blobstore_maintenance`
extlinks['origin']    = ('https://github.com/return42/boilerplate/src/master/%s', 'git')
extlinks['commit']    = ('https://github.com/return42/boilerplate/commit/%s', '#')

# sphinx.ext.imgmath setup
html_math_renderer = 'imgmath'
imgmath_image_format = 'svg'
imgmath_font_size = 14
# sphinx.ext.imgmath setup END


html_search_language = 'de'

sys.path.append(os.path.abspath('_themes'))
html_theme           = "custom"
html_logo            = 'darmarIT_logo_128.png'
html_theme_path      = ['_themes']
html_static_path     = ["static"]


# ------------------------------------------------------------------------------
# Since loadConfig overwrites settings from the global namespace, it has to be
# the last statement in the conf.py file
# ------------------------------------------------------------------------------
load_sphinx_config(globals())
