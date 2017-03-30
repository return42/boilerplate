# -*- coding: utf-8; mode: makefile-gmake -*-

include utils/makefile.include
include utils/makefile.python
include utils/makefile.sphinx

GIT_URL   = https://github.com/return42/boilerplate.git
SLIDES    = docs/slides

all: clean docs

PHONY += help
help:
	@echo  '  docs   - build documentation'
	@echo  '  clean  - remove most generated files'
	@echo  ''
	@$(MAKE) -s -f utils/makefile.sphinx docs-help


PHONY += docs
docs:  sphinx-doc
	$(call cmd,sphinx,html,$(SLIDES),$(SLIDES))

PHONY += clean
clean: pyclean docs-clean
	$(call cmd,common_clean)

.PHONY: $(PHONY)

