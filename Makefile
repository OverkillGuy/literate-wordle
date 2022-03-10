
.PHONY: all
all: install lint docs test build

.PHONY: install
install:
	poetry install


.PHONY: lint
lint:  # Use all linters on all files (not just staged for commit)
	pre-commit run --all --all-files

.PHONY: test
test:
	poetry run pytest

.PHONY: docs
docs: wordle.html
	cd docs && make html

.PHONY: docs-serve
docs-serve:
	cd docs/build/html && python3 -m http.server


.PHONY: build
build:
	poetry build


# Less commonly used commands

# Install poetry from pipx
# Note: pipx is NOT pip, see pipx docs:
# https://pypa.github.io/pipx/
.PHONY: install-poetry
install-poetry:
	pipx install poetry

# Ensure Poetry will generate virtualenv inside the git repo /.venv/
# rather than in a centralized location. This makes it possible to
# manipulate venv more simply.
# This is a global flag for all repos, only need to do this once
.PHONY: poetry-venv-local
poetry-venv-local:
	poetry config virtualenvs.in-project true

# Delete the virtualenv to clean dependencies
# Useful when switching to a branch with less dependencies
# Requires the virtualenv to be local (see "poetry-venv-local")
poetry-venv-nuke:
	find .venv -delete




wordle.html: wordle.org
	emacs --batch \
		--script ~/.emacs.d/init.el \
		--eval "(load-file \"~/.doom.d/init.el\")" \
		--eval "(progn (require 'ox-html) (dolist (file command-line-args-left) (with-current-buffer (find-file-noselect file) (org-html-export-to-html)))))" \
		wordle.org

# Exports this repository as a tarball
# made up of git bundle file (cloneable/pullable file)
# and generated HTML docs
.PHONY: export-repo
export-repo: docs
	git bundle create wordle.gitbundle --all
	tar czvf wordle.tar.gz docs/build/html/ wordle.gitbundle
