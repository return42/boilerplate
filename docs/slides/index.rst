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

.. _make: https://www.gnu.org/software/make/
.. _Sphinx: http://www.sphinx-doc.org
.. _Python: https://www.python.org
.. _Makefile.python_prj: https://github.com/return42/boilerplate/blob/master/Makefile.python_prj


.. revealjs:: Intro

   In my projects I like to run tests and build processes from make_.  The
   boilerplate code here is for common build purpose and heavily based on:

   - make_
   - Sphinx_ (Python_)


.. revealjs:: add boilerplate to your project

   copy ``./utils`` folder to your repository and add some includes to your
   ``./Makefile`` (python projects see Makefile.python_prj_)

   .. rv_code::

      # -*- coding: utf-8; mode: makefile-gmake -*-

      include utils/makefile.include
      include utils/makefile.python
      include utils/makefile.sphinx
      include utils/makefile.0

   In your repository add developer's ``requirements.txt``

   .. rv_code::

      Sphinx
      sphinx_rtd_theme
      sphinx-autobuild
      pip
      git+https://github.com/return42/sphinxjp.themes.revealjs

.. revealjs:: common make options

   .. rv_code::

      $ make make-help
        make V=0|1 [targets] 0 => quiet build (default), 1 => verbose
        make V=2   [targets] 2 => give reason for rebuild of target

.. _makefile.sphinx: https://github.com/return42/boilerplate/blob/master/utils/makefile.sphinx

.. revealjs:: add doc targets to Makefile (1)

   Use definitions from makefile.sphinx_ to define your doc targets.

   .. rv_code::
      :class: Makefile

      help:
          @echo  '  docs      - build documentation'
          @echo  '  docs-live - autobuild HTML doc while editing'
          @$(MAKE) -s -f utils/makefile.include make-help
          @$(MAKE) -s -f utils/makefile.sphinx docs-help

      docs: sphinx-doc
          $(call cmd,sphinx,html,docs,docs)

      docs-live: sphinx-live
          $(call cmd,sphinx_autobuild,html,docs,docs)

   builds (Sphinx) documentation from folder *docs*.

.. revealjs:: add doc targets to Makefile (2)

   build (reveal.js) presentation from folder *docs/slides*.

   .. rv_code::
      :class: Makefile

      slides:  sphinx-doc
              $(call cmd,sphinx,html,docs/slides,docs/slides,slides)

      help:
              @echo  '  slides - build reveal.js slide presentation'

      .PHONY: slides help

   .. rv_small::

      in your requirements.txt use my more up-to-date fork

   .. rv_code::

      git+https://github.com/return42/sphinxjp.themes.revealjs

.. revealjs:: use predefined python targets (1)

   .. rv_code::
      :class: Makefile

      help:
        @echo  '  install   - developer install'
        @echo  '  uninstall - developer uninstall'
        @echo  ''
        @$(MAKE) -s -f utils/makefile.python python-help

      install: pyinstall

      uninstall: pyuninstall

.. revealjs:: use predefined python targets (2)

   .. rv_code::

      $ make help
        install   - developer install
        uninstall - developer uninstall

      makefile.python:
        pylint        - run pylint *linting*
        pytest        - run *tox* test on python objects
        pydebug       - run tests within a PDB debug session
        pybuild       - build python packages
        pyclean       - clean intermediate python objects
        py[un]install - [un]install python objects in editable mode
        upload-pypi   - upload py_dist/* files to PyPi
      options:
        make PY=2  [targets] => to eval targets with python 2 (3)
        make PIP_INST=       => to set/unset pip install options (--user)
        make TEST=.          => choose test from ./tests (default "." runs all)
        make DEBUG=          => target "debug": do not invoke PDB on errors
      when using target "pydebug", set breakpoints within py-source by adding::
          ...
          DEBUG()
          ...

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
