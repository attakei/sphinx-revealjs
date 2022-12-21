# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile demo intl

demo:
	@$(SPHINXBUILD) -b dirrevealjs "$(SOURCEDIR)" "$(BUILDDIR)/demo/ja" $(SPHINXOPTS) $(O) -D language="ja"
	@$(SPHINXBUILD) -b dirrevealjs "$(SOURCEDIR)" "$(BUILDDIR)/demo/en" $(SPHINXOPTS) $(O)
	./gen-index.py $(BUILDDIR)/demo
	touch $(BUILDDIR)/demo/.nojekyll

intl:
	@$(SPHINXBUILD) -M gettext "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	sphinx-intl update --language=ja

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
