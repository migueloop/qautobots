#
# Basic makefile for general targets
#

PACKAGE = qautobots
MODULE = qautobots

# Target environment definitions.  
# Test coverage reports use this environment.

PYTHON_VERSION = python2.7

ACTIVATE = $(ENVDIR)/bin/activate
ENVDIR = ./env
COVERAGE = $(ENVDIR)/bin/coverage
DEVELOPMENT_ENV = configuration/default.json
NOSE = $(ENVDIR)/bin/nosetests
PEP8 = $(ENVDIR)/bin/pep8
PEP257 = $(ENVDIR)/bin/pep257
PIP = C_INCLUDE_PATH="/opt/local/include:/usr/local/include" $(ENVDIR)/bin/pip
PIPOPTS=$(patsubst %,-r %,$(wildcard $(HOME)/.requirements.pip requirements.pip)) --index-url=$(PYTHON_INDEX_URL)
PYLINT = $(ENVDIR)/bin/pylint
PYTHON = $(ENVDIR)/bin/python
PYTHON_INDEX_URL = https://pypi.python.org/simple/
REPORTDIR = reports
SETUP = . $(ACTIVATE); $(PYTHON) setup.py
# Work around a bug in git describe: http://comments.gmane.org/gmane.comp.version-control.git/178169
VERSION = $(shell git status >/dev/null 2>/dev/null && git describe --abbrev=6 --tags --dirty --match="[0-9]*")
VIRTUALENV = virtualenv
VIRTUALENVOPTS = --python=$(PYTHON_VERSION)

APT_REQ_FILE = requirements.apt
DIST_FILE = dist/$(PACKAGE)-$(VERSION).tar.gz
EGG_LINK = $(ENVDIR)/lib/$(PYTHON_VERSION)/site-packages/$(PACKAGE).egg-link

PROCESSES ?= 0
PROCESS_TIMEOUT ?= 8000
EXCLUDE = decepticons.txt
EXCLUDE_SCRIPT = $(MODULE)/utilities/create_exclude_flags.py

## Testing ##
.PHONY: test coverage

test: unit-test integration-test acceptance-test
coverage: unit-coverage

%-test: $(REPORTDIR)
	@echo Running $* tests
	$(DEVELOPMENT_ENV) $(NOSE) --cover-package=$(MODULE),tests --tests=tests/$* --with-xunit --xunit-file=$(REPORTDIR)/$*-xunit.xml

%-coverage: %-test
	@echo Generating $* coverage reports
	$(COVERAGE) html -d $(REPORTDIR)/htmlcov-$* --omit=$(ENVDIR)/*
	$(COVERAGE) xml  -o $(REPORTDIR)/$*-coverage.xml --omit=$(ENVDIR)/*

$(REPORTDIR): $(EGG_LINK)
	test -d "$@" || mkdir -p "$@"
	touch "$@"

## Static Analysis ##
.PHONY: lint pep257 pep8 pylint
lint: pep257 pep8 pylint

pylint: $(REPORTDIR) .tests.pylintrc
	$(PYLINT) --reports=y --output-format=parseable --rcfile=pylintrc $(MODULE) | tee $(REPORTDIR)/$(MODULE)_lint.txt
	$(PYLINT) --reports=y --output-format=parseable --rcfile=.tests.pylintrc tests | tee $(REPORTDIR)/tests_lint.txt

.tests.pylintrc: pylintrc pylintrc-tests-overrides
	cat $^ > $@

pep8: $(REPORTDIR)
	$(PEP8) --filename="*.py" --repeat $(MODULE) tests | tee $(REPORTDIR)/pep8.txt

pep257:
	$(PEP257) $(MODULE) 2>&1 | egrep -v '0: (First line should end with a period|Blank line missing after one-line summary)'

## Local Setup ##
.PHONY: cybertron req virtualenv dev
cybertron:
	@rm -f .req
	$(MAKE) .req

req: .req
.req: $(ENVDIR) requirements.pip
	$(PIP) install $(PIPOPTS)
	@touch .req

setup.py: RELEASE-VERSION
RELEASE-VERSION:
	@echo Updating $@ "($(VERSION))"
	@echo $(VERSION) > $@

dev: $(EGG_LINK)
$(EGG_LINK): setup.py .req
	$(SETUP) develop --index-url=$(PYTHON_INDEX_URL)

virtualenv: $(ENVDIR)
$(ENVDIR):
	$(VIRTUALENV) $(VIRTUALENVOPTS) $(ENVDIR)

## Housekeeping ##
.PHONY: megatron the-fallen unicron
megatron:
	@echo "Removing intermediate files"
	$(RM) RELEASE-VERSION .nose-stopwatch-times .tests.pylintrc pip-log.txt
	$(RM) -r dist disttest *.egg *.egg-info
	find . -type f -name '*.pyc' -delete

the-fallen: megatron
	@echo "Removing output files"
	$(RM) -r $(REPORTDIR) build

unicron: the-fallen
	@echo "Removing all generated and downloaded files"
	$(RM) -r $(ENVDIR)
	$(RM) -r decepticons.txt
	$(RM) -r .noseids
	$(RM) -r .coverage

## Selenium Test Execution ##
autobots-%: $(REPORTDIR)
	@echo Running $*
	$(ENVDIR)/bin/nosetests --tests=$(MODULE)/tests/$(subst -,_,$*) --cover-package=$(MODULE) --nologcapture --processes=$(PROCESSES) -v --process-timeout=$(PROCESS_TIMEOUT) --with-id

decepticons-%: $(REPORTDIR)
	@echo Running $*
	$(ENVDIR)/bin/nosetests --tests=$(MODULE)/tests/$(subst -,_,$*) --cover-package=$(MODULE) --nologcapture --processes=$(PROCESSES) -v --process-timeout=$(PROCESS_TIMEOUT) --failed

.PHONY: autobots-rollout
autobots-rollout: $(REPORTDIR) exclude-flags
	@echo Running all gui-tests
	$(ENVDIR)/bin/nosetests --tests=$(MODULE)/tests/ --cover-package=$(MODULE) --nologcapture --processes=$(PROCESSES) -v --process-timeout=$(PROCESS_TIMEOUT) --exclude-dir-file=$(EXCLUDE)

.PHONY: exclude-flags
exclude-flags: $(REPORTDIR) $(EXCLUDE_SCRIPT)
	$(PYTHON) $(EXCLUDE_SCRIPT) $(EXCLUDE)

-include Makefile.inc

