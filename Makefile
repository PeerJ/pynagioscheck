V := 0
AT_0 := @
AT_1 :=
AT = $(AT_$(V))

SHELL := "/bin/bash"

NOSE := $(shell which nosetests)
SOURCES := Makefile nagioscheck.py \
    $(shell find tests -type f \
    -and -not \( \
	  -name '.*.swp' -or \
	  -name '*.pyc' \
	\) \
)

all: test-stamp

coverage: test-stamp
	$(AT)coverage report -m | tee coverage

test: tests

tests: test-stamp

test-stamp: $(SOURCES)
	$(AT)rm -f .coverage
	$(AT)cat tests/ORDER | while read t; do \
		echo "$${t}:" ; \
		coverage run -a $(NOSE) "$$t" ; \
		echo ; \
	done
	$(AT)touch $@

.PHONY: all coverage test tests
