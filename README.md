# Literate Wordle in Python

Writing up a Python implementation of Wordle using literate programming.

> Follow along on the journey to implement Wordle in Python using TDD

Requires Python >=3.9.

## Literate programming

Literate programming is the practice of writing a program as if it was a novel
or a blog post, with each explanation conjoined with a code block. A process
called "tangling" reorganises the code blocks into their final file paths.

In this case, the "novel" is the file `wordle.org` (written in [org-mode](https://orgmode.org)), and tangles into this repository's entire code.

In terms of code, other than the `wordle.org` file and its mix of code and
prose, and the fact it can re-generate the code files, the rest of the
repository is a completely normal python project.

## Usage

The primary usage of this repository is as a "story" to read along.

To generate that document, use `make docs` to build the project's website, which contains:
- Pretty HTML render of `wordle.org`
- Raw version of `wordle.org` for the curious
- Python module API reference (generated from code tangled out into repo)
- Requirements list, each a Gherkin feature, mapping to test cases

If you want to read the generated document, run `make docs docs-serve` to
generate the document and serve it locally via python's own local HTTP server.

The secondary usage of this repository is as example codebase for the best practices of modern Python development.


### Play the game

Install the module first:

    # Equivalents:
    make install
	poetry install

Then inside the virtual environment, launch the game:

	# Load the virtualenv first
	poetry shell
	# Then launch the game
	pywordle
    # or
    # Run single game inside virtualenv
    poetry run pywordle

### Reuse the python module

Use as any python module:

	# Get a virtualenv going first, such as via poetry
	poetry shell
	python3
	>>> from literate_wordle import words
	>>> words.pick_answer_word()
	blank

## Development

### Python setup

This repository uses Python 3.9 or above, using
[Poetry](https://python-poetry.org) as package manager to define a Python
package inside `src/literate_wordle/`.

`poetry` will create virtual environments if needed, fetch
dependencies, and install them for development.

This codebase uses [pre-commit](https://pre-commit.com) to run linting tools
like `flake8`, and formatters like `black`. Use `pre-commit install` to install
git pre-commit hooks to force running these checks before any code can be
committed, use `make lint` to run these manually. Testing is provided by
`pytest` separately in `make test`.

Installation of `poetry` and `pre-commit` is recommended via
[pipx](https://pypa.github.io/pipx/).


For ease of development, a `Makefile` is provided, use it like this:

	make  # equivalent to "make all" = install lint docs test build
	# run only specific tasks:
	make install
	make lint
	make test
	# Combine tasks:
	make install test

### Documentation

Documentation is generated via [Sphinx](https://www.sphinx-doc.org/en/master/), using the cool [myst_parser](https://myst-parser.readthedocs.io/en/latest/) plugin to support Markdown files like this one.

Other Sphinx plugins provide extra documentation features, like the fantastic [sphinxcontrib-needs](https://sphinxcontrib-needs.readthedocs.io/en/latest/index.html) used to track project requirements, the recent [AutoAPI](https://sphinx-autoapi.readthedocs.io/en/latest/index.html) to generate API reference without headaches, and the experimental [sphinx-collections](https://sphinx-autoapi.readthedocs.io/en/latest/index.html) to include automatically generated documentation.

To build the documentation, run

    # Requires the project dependencies provided by "make install"
    make docs

To browse the website version of the documentation you just built, run:

    make docs-serve

And remember that `make` supports multiple targets, so you can generate the documentation and serve it:

    make docs docs-serve


## License

This project is released under GPLv3. See `COPYING` file for GPLv3 license
details.
