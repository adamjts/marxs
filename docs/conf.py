# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#
# Astropy documentation build configuration file.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this file.
#
# All configuration values have a default. Some values are defined in
# the global Astropy configuration which is loaded here before anything else.
# See astropy.sphinx.conf for which values are set there.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('..'))

# IMPORTANT: the above commented section was generated by sphinx-quickstart, but
# is *NOT* appropriate for astropy or Astropy affiliated packages. It is left
# commented out with this explanation to make it clear why this should not be
# done. If the sys.path entry above is added, when the astropy.sphinx.conf
# import occurs, it will import the *source* version of astropy instead of the
# version installed (if invoked as "make html" or directly with sphinx), or the
# version in the build directory (if "python setup.py build_sphinx" is used).
# Thus, any C-extensions that are needed to build the documentation will *not*
# be accessible, and the documentation will not build correctly.

import datetime
import os
import sys

try:
    import astropy_helpers
except ImportError:
    # Building from inside the docs/ directory?
    if os.path.basename(os.getcwd()) == 'docs':
        a_h_path = os.path.abspath(os.path.join('..', 'astropy_helpers'))
        if os.path.isdir(a_h_path):
            sys.path.insert(1, a_h_path)

# Load all of the global Astropy configuration
from astropy_helpers.sphinx.conf import *

# Get configuration information from setup.cfg
from distutils import config
conf = config.ConfigParser()
conf.read([os.path.join(os.path.dirname(__file__), '..', 'setup.cfg')])
setup_cfg = dict(conf.items('metadata'))

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.2'

# To perform a Sphinx version check that needs to be more specific than
# major.minor, call `check_sphinx_version("x.y.z")` here.
# check_sphinx_version("1.2.1")

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns.append('_templates')

# This is added to the end of RST files - a good place to put substitutions to
# be used globally.
rst_epilog += """
"""

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions += [
#    'sphinx.ext.mathjax',
#    'sphinx.ext.napoleon',
#    'sphinx.ext.autosummary',
#    'matplotlib.sphinxext.plot_directive',
#]

numpydoc_show_class_members = False
todo_include_todos = True


# -- Project information ------------------------------------------------------

# This does not *have* to match the package name, but typically does
project = setup_cfg['package_name']
author = setup_cfg['author']
copyright = '{0}, {1}'.format(
    datetime.datetime.now().year, setup_cfg['author'])

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

__import__(setup_cfg['package_name'])
package = sys.modules[setup_cfg['package_name']]

# The short X.Y version.
version = package.__version__.split('-', 1)[0]
# The full version, including alpha/beta/rc tags.
release = package.__version__

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = 'any'

# Add this to the top of every file
rst_epilog += '''
.. _classic marx: http://space.mit.edu/cxc/marx/
'''

#autosummary_generate = True

# -- Options for HTML output ----------------------------------------------
# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']


# Output file base name for HTML help builder.
htmlhelp_basename = 'Marxsdoc'

# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [('index', project + '.tex', project + u' Documentation',
                    author, 'manual')]


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [('index', project.lower(), project + u' Documentation',
              [author], 1)]


## -- Options for the edit_on_github extension ----------------------------------------

if eval(setup_cfg.get('edit_on_github')):
    extensions += ['astropy_helpers.sphinx.ext.edit_on_github']

    versionmod = __import__(setup_cfg['package_name'] + '.version')
    edit_on_github_project = setup_cfg['github_project']
    if versionmod.version.release:
        edit_on_github_branch = "v" + versionmod.version.version
    else:
        edit_on_github_branch = "master"

    edit_on_github_source_root = ""
    edit_on_github_doc_root = "docs"
