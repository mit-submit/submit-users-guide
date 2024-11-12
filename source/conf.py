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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import warnings
from sphinx.deprecation import RemovedInSphinx90Warning

warnings.filterwarnings("ignore", category=RemovedInSphinx90Warning)




# -- Project information -----------------------------------------------------

project = 'subMIT'
copyright = '2021, The SubMIT Project Team'
author = 'The SubMIT Project Team'

# The full version, including alpha/beta/rc tags
release = 'v1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_toolbox.collapse',
    'sphinx_tabs.tabs',
    'sphinx_togglebutton',
    'sphinx_design',
    'sphinx_tags'
]




tags_create_tags = True
tags_create_badges = True
tags_badge_colors = {
        "Julia": "primary",
        "Mathematica": "secondary",
        "Conda": "success",
        "Slurm": "info",
        "Condor": "warning",
        "Containers": "danger",
        "VSCode": "light",
        "JupyterHub": "dark"
}

tags_page_title = "All tags"
tags_page_header = "Tags in this site"
tags_overview_title = "User's Guide Tags"
tags_page_path = '_tags'
tags_index_page = 'tagsindex'
tags_index_head = "Click on a word to see the pages referring to this tag. The number in parenthesis is the number of pages with this tag."
tags_create_tags_index = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

#html_theme = 'alabaster'
#html_theme = 'sizzle'
html_theme = 'groundwork'

#Theme options for groundwork: https://github.com/useblocks/groundwork-sphinx-theme
html_theme_options = {
#    "sidebar_width": '240px',
    "stickysidebar": True,
    "stickysidebarscrollable": True,
#    "contribute": True,
#    "github_fork": "useblocks/groundwork",
#    "github_user": "useblocks",
}

#import sphinx_adc_theme
#html_theme = 'sphinx_adc_theme'
#html_theme_path = [sphinx_adc_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []
#html_logo = 'img/submit-logo-construction.png'
html_logo = 'img/submit-nnnext-logo.png'
html_favicon = 'img/submit-nnnext-logo.png'
