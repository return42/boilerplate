# -*- coding: utf-8; mode: makefile-gmake -*-

include utils/makefile.include
include utils/makefile.python
include utils/makefile.sphinx
include utils/makefile.0

GIT_URL   = https://github.com/return42/boilerplate.git
SLIDES    = docs/slides

all: clean docs

PHONY += help help-min help-all

help: help-min
	@echo  ''
	@echo  'to get more help:  make help-all'

help-min:
	@echo  '  docs      - build documentation'
	@echo  '  docs-live - autobuild HTML documentation while editing'
	@echo  '  clean     - remove most generated files'
	@echo  '  install   - developer install (./local)'
	@echo  '  uninstall - uninstall (./local)'
	@echo  ''
	$(Q)$(MAKE) -e -s make-help

help-all: help-min
	@echo  ''
	$(Q)$(MAKE) -e -s docs-help
	@echo  ''
	$(Q)$(MAKE) -e -s python-help

PHONY += install
install: pyenvinstall

PHONY += uninstall
uninstall: pyenvuninstall

PHONY += docs
docs:  install slides
	$(call cmd,sphinx,html,$(DOCS_FOLDER),$(DOCS_FOLDER))

PHONY += slides
slides:  install
	$(call cmd,sphinx,html,$(SLIDES),$(SLIDES),slides)

PHONY += docs-live
docs-live: install sphinx-live
	$(call cmd,sphinx_autobuild,html,$(DOCS_FOLDER),$(DOCS_FOLDER))

PHONY += clean
clean: pyclean docs-clean
	$(call cmd,common_clean)

PHONY += project
project: $(PY_ENV) pyenvinstall
	@echo '  PROJECT   requirements.txt'
	$(Q)- rm -f requirements.txt
	$(Q)$(PY_ENV_BIN)/python -c "from XXXX.__pkginfo__ import *; print(requirements_txt)" > ./requirements.txt
	#$(Q)- rm -f README.rst
	#@echo '  PROJECT   README.rst'
	#$(Q)$(PY_ENV_BIN)/python -c "from XXXX.__pkginfo__ import *; print(README)" > ./README.rst

.PHONY: $(PHONY)

