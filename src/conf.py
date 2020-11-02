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
import ablog


# -- Project information -----------------------------------------------------

project = 'Urban Grammar AI'
copyright = '2020, Dani Arribas-Bel, Martin Fleischmann'
author = 'Dani Arribas-Bel, Martin Fleischmann'

# -- General ABlog Options ----------------------------------------------------

# A path relative to the configuration directory for blog archive pages.
#blog_path = 'blog'

# The "title" for the blog, used in active pages.  Default is ``'Blog'``.
blog_title = u'Urban Grammar AI Blog'

# Base URL for the website, required for generating feeds.
# e.g. blog_baseurl = "http://example.com/"
blog_baseurl = u'https://urbangrammarai.github.io/'

# Choose to archive only post titles. Archiving only titles can speed
# up project building.
#blog_archive_titles = False

# -- Blog Authors, Languages, and Locations -----------------------------------

# A dictionary of author names mapping to author full display names and
# links. Dictionary keys are what should be used in ``post`` directive
# to refer to the author.  Default is ``{}``.
blog_authors = {}


# A dictionary of language code names mapping to full display names and
# links of these languages. Similar to :confval:`blog_authors`, dictionary
# keys should be used in ``post`` directive to refer to the locations.
# Default is ``{}``.
#blog_languages = {
#    'en': ('English', None),
#}


# A dictionary of location names mapping to full display names and
# links of these locations. Similar to :confval:`blog_authors`, dictionary
# keys should be used in ``post`` directive to refer to the locations.
# Default is ``{}``.
#blog_locations = {
#    'Earth': ('The Blue Planet', 'https://en.wikipedia.org/wiki/Earth),
#}

# -- Blog Post Related --------------------------------------------------------

# Format date for a post.
#post_date_format = '%b %d, %Y'

# Number of paragraphs (default is ``1``) that will be displayed as an excerpt
# from the post. Setting this ``0`` will result in displaying no post excerpt
# in archive pages.  This option can be set on a per post basis using
post_auto_excerpt = 5

# Index of the image that will be displayed in the excerpt of the post.
# Default is ``0``, meaning no image.  Setting this to ``1`` will include
# the first image, when available, to the excerpt.  This option can be set
# on a per post basis using :rst:dir:`post` directive option ``image``.
#post_auto_image = 0

# Number of seconds (default is ``5``) that a redirect page waits before
# refreshing the page to redirect to the post.
#post_redirect_refresh = 5

# When ``True``, post title and excerpt is always taken from the section that
# contains the :rst:dir:`post` directive, instead of the document. This is the
# behavior when :rst:dir:`post` is used multiple times in a document. Default
# is ``False``.
#post_always_section = False

# When ``False``, the :rst:dir:`orphan` directive is not automatically set
# for each post. Without this directive, Sphinx will warn about posts that
# are not explicitly referenced via another document. :rst:dir:`orphan` can
# be set on a per-post basis as well if this is false. Default is ``True``.
#post_auto_orphan = True

# -- ABlog Sidebars -------------------------------------------------------

# There are seven sidebars you can include in your HTML output.
# postcard.html provides information regarding the current post.
# recentposts.html lists most recent five posts. Others provide
# a link to a archive pages generated for each tag, category, and year.
# In addition, there are authors.html, languages.html, and locations.html
# sidebars that link to author and location archive pages.
html_sidebars = {
    '**': [ 
            'archives.html',
            ],
    }

# -- Blog Feed Options --------------------------------------------------------

# Turn feeds by setting :confval:`blog_baseurl` configuration variable.
# Choose to create feeds per author, location, tag, category, and year,
# default is ``False``.
#blog_feed_archives = False

# Choose to display full text in blog feeds, default is ``False``.
#blog_feed_fulltext = False

# Blog feed subtitle, default is ``None``.
#blog_feed_subtitle = None

# Choose to feed only post titles, default is ``False``.
#blog_feed_titles = False

# Specify number of recent posts to include in feeds, default is ``None``
# for all posts.
#blog_feed_length = None

# -- Font-Awesome Options -----------------------------------------------------

# ABlog templates will use of Font Awesome icons if one of the following
# is ``True``

# Link to `Font Awesome`_ at `Bootstrap CDN`_ and use icons in sidebars
# and post footers.  Default: ``None``
#fontawesome_link_cdn = None

# Sphinx_ theme already links to `Font Awesome`_.  Default: ``False``
#fontawesome_included = False

# Alternatively, you can provide the path to `Font Awesome`_ :file:`.css`
# with the configuration option: fontawesome_css_file
# Path to `Font Awesome`_ :file:`.css` (default is ``None``) that will
# be linked to in HTML output by ABlog.
#fontawesome_css_file = None

# -- Disqus Integration -------------------------------------------------------

# You can enable Disqus_ by setting ``disqus_shortname`` variable.
# Disqus_ short name for the blog.
#disqus_shortname = None

# Choose to disqus pages that are not posts, default is ``False``.
#disqus_pages = False

# Choose to disqus posts that are drafts (without a published date),
# default is ``False``.
#disqus_drafts = False

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    'ablog',
    'sphinx.ext.intersphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
templates_path.append(ablog.get_html_templates_path())

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    "external_links": [
        ("Github", "https://github.com/urbangrammarai"),
        ("Turing", "https://www.turing.ac.uk/research/research-projects/urban-grammar")
  ]
}

html_css_files = [
    'custom.css',
]

html_logo = "_static/logo.svg"
