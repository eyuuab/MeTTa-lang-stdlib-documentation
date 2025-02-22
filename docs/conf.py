# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sphinx_rtd_theme


project = 'MeTTa Standard Library'
copyright = '2025, Eyobed A.'
author = 'Eyobed A.'
release = '0.1'

extensions = ["myst_parser"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_js_files = [
    "js/jquery.min.js",  
    "searchtools.js"     
]


html_static_path = ['_static']
html_search_language = 'en'

html_favicon = "_static/favicon.ico"
html_logo = "_static/logo.png"

html_css_files = ["custom.css"]
templates_path = ["_templates"]

