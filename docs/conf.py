# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "MATH/CODE"
copyright = "2024, Alejandro Sánchez Yalí"
author = "Alejandro Sánchez Yalí"
release = "0.1"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "nbsphinx",
    "sphinx.ext.mathjax",
    "sphinx_gallery.load_style",  # load CSS for gallery (needs SG >= 0.6)
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "notebooks/tutorial*/*_empty.ipynb",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"

html_theme_options = {
    "collapse_navigation": True,
    "navigation_depth": 4,
    "repository_url": "https://github.com/asanchezyali/math-code",
    "use_repository_button": True,
    "use_sidenotes": True,
}

html_context = {
    "display_github": True,
    "github_user": "asanchezyali",
    "github_repo": "math-code",
    "github_version": "main/docs/",
}

html_title = "MATH / CODE"

html_static_path = ["_static"]

master_doc = "index"

highlight_language = "python3"

nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]
