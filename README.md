# Literate Wordle in Python

Writing a Python Wordle implementation as a literate program.

Requires Python >3.8.

## Literate programming

Literate programming is the practice of writing a program as if it was a novel
or a blog post, with each explanation conjoined with a code block. A process
called "tangling" extracts the code blocks to be generated into proper files.

In this case, the novel is available in [wordle.org](./wordle.org), and tangles
into this repository's code.

Other than this file duplicating the entire repo's worth of code, the rest of
this repo is normal.

## Usage

Run the per-day scripts with your own custom input:

	# Get a virtualenv going first, such as via poetry
	poetry shell
	# Now play!
	pywordle

## Development

### Python setup

This repository uses Python>3.8, using [Poetry](https://python-poetry.org) as
package manager to define a Python package inside `src/literate_wordle/`.

`poetry` will create virtual environments if needed, fetch
dependencies, and install them for development.

This codebase uses [pre-commit](https://pre-commit.com) to run linting
tools like `flake8`.Use `pre-commit install` to install git pre-commit
hooks to force running these checks before any code can be committed,
use `make lint` to run these manually. Testing is provided by `pytest`
separately in `make test`.

Installation of `poetry` and `pre-commit` is recommended via
[pipx](https://pypa.github.io/pipx/).


For ease of development, a `Makefile` is provided, use it like this:

	make  # equivalent to "make all" = install lint test build
	# run only specific tasks:
	make install
	make lint
	make test
	# Combine tasks:
	make install test

Once installed, the module's code can now be reached through running
Python in Poetry:

	$ poetry run python
	>>> import literate_wordle
	>>> print(literate_wordle.__version__)
	0.1.0



### Testing

With the development tools set up, run pytest to see test results:

	pytest
