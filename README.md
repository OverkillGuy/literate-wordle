# Literate Wordle in Python

Writing up a Python implementation of Wordle using literate programming.

> Follow along on the journey to implement Wordle in Python using Behaviour-driven Development techniques.

### Dependencies

- [Python](https://www.python.org/) 3.9 or later (use of typing hints)
- [Poetry](https://python-poetry.org) package manager, to install development
  dependencies and generate virtual environment.

Note that the wordle program itself doesn't use any external dependency, but the
way to call that executable as command line tool does depend on Poetry.
Generating project documentation also requires dependencies.

## Literate programming?

Literate programming is the practice of writing a program as if it was a novel
or a blog post, with each explanation conjoined with a code block. A process
called "tangling" extracts the code blocks from text, generating the program's
source code.

In this case, the "novel" is the file `wordle.org` (written in
[org-mode](https://orgmode.org)), and "tangles" most of the repository's source
code folders (mostly `src/`, `features/`, and `tests/`).

In terms of code repository, other than the `wordle.org` file and its mix of
code and prose, and the fact this file can re-generate the project's source
code, the rest of the repository is a completely normal python project.

## Usage

### Read the story

The primary usage of this repository is as a "story" to read along as a webpage.

To generate that document, use `make docs` to build the project's website, which contains:
- Pretty HTML render of `wordle.org` to follow along
- Python module API reference (generated from code tangled out into repo)
- Project's requirements list, each a Gherkin feature, mapping to test cases
- Raw version of `wordle.org` for the curious

If you want to read the generated document, run `make docs docs-serve` to
generate the document and serve it locally via python's own local HTTP server.

The secondary usage of this repository is as example codebase for best practices
of modern Python development.

### Play the game

Install the module first:

    make install
    # or
	poetry install

Then inside the virtual environment, launch the game:

    # Run single game inside virtualenv
    poetry run pywordle

    # or
    # Load the virtualenv first
    poetry shell
    # Then launch the game, staying in virtualenv
    pywordle

### Reuse the python module

Use this package as you would any python module:

	# Get a virtualenv going first, such as via poetry
	poetry shell
	python3
	>>> from literate_wordle import words
	>>> answer = words.pick_answer_word()
    >> print(f"Hello! The secret wordle answer is '{answer}'.")
    Hello! The secret wordle answer is 'blank'.

## Development

### Python setup

This repository uses Python 3.9 or above, using
[Poetry](https://python-poetry.org) as package manager to define a Python
package inside `src/literate_wordle/`.

`poetry` will create virtual environments if needed, fetch
dependencies, and install them for development.

This codebase uses [pre-commit](https://pre-commit.com) to run linting tools
like `flake8`, formatters like `black`, and type checking via `mypy`.

Use `pre-commit install` to install git pre-commit hooks to force running these
checks before any code can be committed, use `make lint` to run these manually.

Testing is provided by `pytest` separately in `make test`.

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
