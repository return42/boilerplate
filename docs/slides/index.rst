=================================================
boilerplate
=================================================

.. raw:: html

   <aside id="logo" style="height:8vh; width:8vw; position:absolute; bottom:2vh; left:2vw; ">
     <a href="http://www.darmarit.de">
       <img src="_static/darmarIT_logo_512.png">
     </a>
   </aside>


.. revealjs:: boilerplate
   :title-heading: h2

   nothing special here, only some of my boilerplates

   .. rv_small::

      *Hit '?' to see keyboard shortcuts*

   `boilerplate@GitHub <https://github.com/return42/boilerplate>`_

   .. rv_small::

      contributed by `return42 <http://github.com/return42>`_


.. revealjs:: add boilerplate to your project

   copy 'utils' folder to your repository and add some includes to your
   Makefile:

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

   .. rv_code::

      PHONY += docs
      docs:  sphinx-doc
              $(call cmd,sphinx,html,docs,docs)

      PHONY += help
      help:
              @echo  '  docs   - build documentation'

      .PHONY: $(PHONY)

   builds (Sphinx) documentation from folder *docs*.

.. revealjs:: add *slides* target to your project

   build (reveal.js) presentation from folder *docs/slides*.

   .. rv_code::

      PHONY += slides
      slides:  sphinx-doc
              $(call cmd,sphinx,html,docs/slides,docs/slides,slides)

      PHONY += help
      help:
      	      @echo  '  slides - build reveal.js slide presentation'

      .PHONY: $(PHONY)


   .. rv_small::

      in your requirements.txt use my more up-to-date fork

   .. rv_code::
      
      git+https://github.com/return42/sphinxjp.themes.revealjs

   
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

.. revealjs:: Thanks!
 :title-heading: h2
 :subtitle-heading: h3
 :subtitle: more slides comming soon ...
