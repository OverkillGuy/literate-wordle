"""Tests for literate_wordle.

By having this init file here, we declare the local folder as a python module. This
allows imports as the folder's name = "tests".

This is very useful to put reusable (common across tests) data and fixtures, in a way
that can be imported cleanly. If we have a file here called "samples.py", we can now do
"from tests.samples import MY_COMMON_DATA".

"""
