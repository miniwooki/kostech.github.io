# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'KOSTECH Documentation'
copyright = '2023, cwjun'
author = 'cwjun'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_design',
    'rst2pdf.pdfbuilder'
]
myst_heading_anchors = 3
# myst_all_links_external = True
templates_path = ['_templates']
exclude_patterns = []
myst_enable_extensions = [
    "colon_fence", 
    "attrs_inline",
    "deflist",
    "attrs_block",
]

myst_number_code_blocks = ["Bash"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

## 추가
import os
import sys
# from recommonmark.parser import CommonMarkParser

# source_parsers = {
#     '.md': CommonMarkParser,
# }
html_css_files = [
    'my_theme.css'
]
# source_suffix = ['.rst','.md']

sys.path.insert(0, os.path.abspath('../../src/my_package'))

# -- Options for LaTeX output ------------------------------------------------
latex_engine = 'xelatex'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': '',

    # Latex figure (float) alignment
    #
    'figure_align': 'htbp',


    # kotex config
    'figure_align': 'htbp',

    'fontpkg': r'''
\usepackage{kotex}

% 영문 폰트 설정
\setmainfont[Mapping=tex-text]{NanumGothic}
\setsansfont[Mapping=tex-text]{나눔명조}
\setmonofont{나눔고딕코딩}

% 한글 폰트 설정
\setmainhangulfont[Mapping=tex-text]{NanumGothic}
\setsanshangulfont[Mapping=tex-text]{나눔명조}
\setmonohangulfont{나눔고딕코딩}

''',
}