
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

# Not a phony target = real file!
wordle_solve.db:
	poetry run python src/literate_wordle/sqlite_solve.py



# Proper Makefile target:
# The file wordle.html is actually generated from wordle.org with that command
# Note: Any modifications (last edit time) of wordle.org will cause rebuild wordle.html
# FIXME: This make target WORKS (generates valid HTML) but result is monochrome = ugly.
# Way less pretty than just using my own Emacs and export HTML myself via
# shortcut `C-c C-e h h`. Despite meaning to be an automated replacement,
# something to do with Doom Emacs init process causes the theming to not load
# theme properly before running HTML export, so the code blocks export as
# monochrome. So keep this command here as fallback, but I'll keep exporting by
# hand till I understand Emacs more.
wordle.html: wordle.org
	emacs --batch \
		--script ~/.emacs.d/init.el \
		--eval "(load-file \"~/.doom.d/init.el\")" \
		--eval "(progn (require 'ox-html) (dolist (file command-line-args-left) (with-current-buffer (find-file-noselect file) (org-html-export-to-html)))))" \
		wordle.org

# FIXME: This make target does export code, but the code layout is wrong, failing linters!
# Some default config of my Doom Emacs seems to influence code
# indentation? So the tangle shortcut `C-c C-v t` in my Emacs give different
# result than this command. Until I understand more about this, use manual
# tangle via shortcut instead!
.PHONY: tangle-code
tangle-code:
	emacs -Q \
		--batch \
		--eval "(progn (require 'ob-tangle) (dolist (file command-line-args-left) (with-current-buffer (find-file-noselect file) (org-babel-tangle))))" \
		wordle.org


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
.PHONY: poetry-venv-nuke
poetry-venv-nuke:
	find .venv -delete


# Exports this repository as a tarball
# made up of git bundle file (cloneable/pullable file)
# and generated HTML docs (serve-able via python3 -m http.server)
.PHONY: export-repo
export-repo: docs
	git bundle create wordle.gitbundle --all
	tar czvf wordle.tar.gz docs/build/html/ wordle.gitbundle
