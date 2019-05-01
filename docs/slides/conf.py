# -*- coding: utf-8 -*-
#
# -- General configuration ----------------------------------------

source_suffix = '.rst'
master_doc = 'index'

project = u'boilerplate'
copyright = u'2017, return42'

version = '1.0.0'

# -- Options for HTML output --------------------------------------

extensions = ['sphinxjp.themes.revealjs']
html_theme = 'revealjs'
html_use_index = False

# -- HTML theme options for `revealjs` style ---------------------

html_theme_options = {

    # For avilable options see:
    # - https://github.com/tell-k/sphinxjp.themes.revealjs#customize-config

    'lang': 'de',
    'theme': 'dejavu',
    'transition': 'slide',
    'slide_number': True,

    # loading custom js after RevealJs.initialize.
    "customjs": "mysettings.js",

    # loading custom css
    "customcss": "mysettings.css",
}

html_static_path = ['_static']
