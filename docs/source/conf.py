# Configuration file for the Sphinx documentation builder.

#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))


# -- Project information -----------------------------------------------------

project = "Literate Wordle"
copyright = "2022, Jb Doyon"
author = "Jb Doyon"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.autodoc",
              "sphinx.ext.autosummary",
              "sphinx.ext.autosectionlabel",
              "sphinx.ext.viewcode",
              "autoapi.extension",
              "sphinxcontrib.collections",
              "sphinxcontrib.needs",
              "sphinxcontrib.plantuml", # dep of sphinxcontrib-needs[1]
              "myst_parser"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


autoapi_type = 'python'
autoapi_dirs = ['../../src']


# Make sure the target is unique
autosectionlabel_prefix_document = True

myst_heading_anchors = 2

# Sphinx-Collections Extension


def list_features(features_full_path):
    """Generate a sphinxcontrib-collection-compatible dict of features files

    Lists out files under a specific features path, giving out a dictionary made
    up of list of feature file details (dict)
    """
    file_list = os.listdir(features_full_path)
    return {"features": [({"filename": filename}) for filename in file_list]}


FEATURES_FOLDERNAME = "features"
FEATURES_RELATIVE_PATH = ".."
FEATURES_FULL_PATH = f"{FEATURES_RELATIVE_PATH}/{FEATURES_FOLDERNAME}/"

collections = {
    'wordle_html_export_filecopy': {
      'driver': 'copy_file',
      'source': f"../wordle.html",
      'target': '_static/wordle.html'
    },
    'gherkin_features_foldercopy' : {
        'driver': 'copy_folder',
        'source': FEATURES_FULL_PATH,  # one up from the docs/ folder (where "make" runs)
        'target': 'gherkin_features/',
        'ignore': ['*.md', '*.org'], # Copy only ".feature" really
    },
    'gherkin_features_jinja': {
        'driver': 'jinja',
        'source': '_templates/gherkin_feature.md.j2',
        'target': 'gherkin_feature.md',
        'multiple_files': False,  # Single output file, loops INSIDE jinja template
        'data': list_features(f"../{FEATURES_FULL_PATH}") # listdir is run at conf.py instead = more up
    },
}

# Sphinxcontrib-plantuml

# I haven't really installed plantuml, and as long as I don't need it for
# sphinxcontrib-needs, it won't bother me to point to a fake file.
# Ideally, plantuml would be an optional dependency of sphinxcontrib-needs[1]
# [1]: https://github.com/useblocks/sphinxcontrib-needs/issues/222
plantuml_jar_path = "/dev/null"
