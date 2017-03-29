=================================================
boilerplate
=================================================

.. revealjs:: boilerplate
   :title-heading: h2
   :subtitle: nothing special here, only some of my boilerplates
   :subtitle-heading: h3

   .. rv_small::

      Created by `return42 <http://github.com/return42>`_

.. revealjs:: About this presentation

   This is a small `REVAL.JS <http://lab.hakim.se/reveal-js>`_ presentation.
   The source format of it's content is in `reST-markup
   <http://docutils.sourceforge.net/rst.html>`_.

   The HTML is build by the `Sphinx-doc <http://www.sphinx-doc.org/>`_ extension
   `sphinxjp.themes.revealjs <https://github.com/tell-k/sphinxjp.themes.revealjs>`_.

   .. rv_small::

      Hit **s** on your keyboard to see the speaker notes.

   .. rv_note::

      These are some notes. They'll be hidden in your presentation, but
      you can see them if you open the speaker notes window .

      #. sphinxjp.themes.revealjs: https://github.com/tell-k/sphinxjp.themes.revealjs
      #. REVEAL.JS: http://lab.hakim.se/reveal-js
      #. Sphinx-doc: http://www.sphinx-doc.org
      #. reST:  http://www.sphinx-doc.org/en/stable/rest.html / http://docutils.sourceforge.net/rst.html


.. revealjs:: add boilerplate to your project

   copy 'util' folder to your repository and add some includes to your Makefile:

   .. rv_code::

      # -*- coding: utf-8; mode: makefile-gmake -*-

      include utils/makefile.include
      include utils/makefile.python
      include utils/makefile.sphinx

   In your repository add developer's requirements.txt

   .. rv_code::

      pip
      sphinx_rtd_theme
      git+https://github.com/return42/sphinxjp.themes.revealjs

.. revealjs:: this is what you get

   .. rv_code::

      $ make help

      makefile.python:
        pylint        - run pylint *linting*
        pytest        - run nose test on python objects
        pybuild       - build python packages
        pyclean       - clean intermediate python objects
        py[un]install - [un]install python objects in editable mode
        upload-pypi   - upload py_dist/... files to PyPi

      makefile.docs:
         docs-clean	- clean intermediate doc objects
         gh-pages	- create & upload github pages

.. revealjs:: add *docs* target to your project

   Build Sphinx documentation from folder *docs*.

   .. rv_code::

      PHONY += docs
      docs:  sphinx-doc
              $(call cmd,sphinx,html,docs,docs)

      PHONY += help
      help:
              @echo  '  docs   - build documentation'

      .PHONY: $(PHONY)


.. revealjs:: add *slides* target to your project

   Build slide presentation from folder *docs/slides*.

   .. rv_code::

      PHONY += slides
      slides:  sphinx-doc
              $(call cmd,sphinx,html,docs/slides,docs/slides,slides)

      PHONY += help
      help:
      	      @echo  '  slides - build reveal.js slide presentation'

      .PHONY: $(PHONY)


.. revealjs:: THE END
 :title-heading: h2
 :subtitle-heading: h3
 :subtitle: BY return42
