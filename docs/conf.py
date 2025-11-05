

project = 'In-silico protocols for Machine Learning Reproducibility'
copyright = 'Creative Commons Attribution 4.0 International Public License'
author = 'Dhwani Solanki, Leyla Jael Castro, Dietrich Rebholz-Schuhmann'



# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",            # MyST Markdown
    "sphinx.ext.mathjax",
    "sphinxcontrib.mermaid"# math support
]

# MyST: allow fenced directives like ```{toctree} and ```{raw} html
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "amsmath",
]
html_theme_options = {
    "repository_url": "https://github.com/zbmed-semtec/in-silico-protocols-4ML",
    "use_repository_button": True,       # shows GitHub icon top-right
    "use_edit_page_button": False,       # set True if you want "Edit this page"
    "use_issues_button": True,           # adds "Open issue" icon
    "home_page_in_toc": True,
    "path_to_docs": "docs",              # path relative to repo root
    "extra_footer": """
      <div><hr/><table align="center" style="width:100%"><tr>
        <td><a href="https://www.zbmed.de/en/legal-notice" target="_blank">Legal notice</a></td>
        <td><a href="https://www.zbmed.de/en/disclaimer" target="_blank">Disclaimer</a></td>
        <td><a href="https://www.zbmed.de/en/privacy-policy" target="_blank">Privacy policy</a></td>
      </tr></table></div>
    """,


 # ---- Custom header icons ----
    "icon_links": [
        {
            "name": "Creative Commons License",
            "url": "https://github.com/zbmed-semtec/in-silico-protocols-4ML/blob/main/LICENSE",
            "icon": "fa-brands fa-creative-commons",  # Font Awesome CC icon
        },
    ],
}
# Treat fenced ```mermaid blocks as the mermaid directive
myst_fence_as_directive = ["mermaid"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- HTML --------------------------------------------------------------------
html_theme = "sphinx_book_theme"
html_title = project
html_static_path = ["_static"]  # <-- needed so our CSS is copied



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"



html_static_path = ["/_static".lstrip("/")]  # equals ["_static"]

# Optional: control Mermaid JS (version/theme). Defaults usually work.
mermaid_version = "10.4.0"
# mermaid_init_js = "mermaid.initialize({startOnLoad:true, theme:'default'});"
