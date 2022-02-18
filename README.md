# Literate Wordle in Python

Writing up a Python implementation of Wordle using literate programming.

> Follow along on the journey to implement Wordle in Python using TDD

Requires Python >3.8.

## Literate programming

Literate programming is the practice of writing a program as if it was a novel
or a blog post, with each explanation conjoined with a code block. A process
called "tangling" reorganises the code blocks into their final file paths.

In this case, the "novel" is the file `wordle.org` (written in [org-mode](https://orgmode.org)), and tangles into this repository's entire code.

As far as programming goes, other than the `wordle.org` file containing the
entire repo's worth of code, the rest of this repo works as any other does.

## Usage

The primary usage of this repository is as a "story" to read along.

To generate that document, use `make docs` to build the project's website, which contains:
- Pretty HTML render of `wordle.org`
- Raw version of `wordle.org` for the curious
- Python module API reference (generated from code tangled out into repo)
- Requirements list, each a Gherkin feature, mapping to test cases

### Python module

Use as any python module:

	# Get a virtualenv going first, such as via poetry
	poetry shell
	python3
	>>> from literate_wordle import words
	>>> words.pick_answer_word()
	blank

## Development

### Python setup

This repository uses Python >3.8, using [Poetry](https://python-poetry.org) as
package manager to define a Python package inside `src/literate_wordle/`.

`poetry` will create virtual environments if needed, fetch
dependencies, and install them for development.

This codebase uses [pre-commit](https://pre-commit.com) to run linting tools
like `flake8`, and formatters like `black`.Use `pre-commit install` to install
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

## License

This project is released under GPLv3. See `COPYING` file for GPLv3 license
details.
