"""Basic tests of literate_wordle"""

from literate_wordle import __version__


def test_version():
    """Checks version matches."""
    assert __version__ == "0.1.0"
