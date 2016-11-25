# rst-citations-to-raw-latex

This repository contains a Python 3 program, which parses reStructuredText files to convert contained citations into raw Latex citations, in order to enable them in the conversion from `reStructuredText` to `PDF` using `Pandoc` and `latexmk`. It also enables page numbers in citations for example written as follows:

    [Source2010 p. 10]_

Note however, that at the moment the program requires the beginning of a line `^` or an arbitrary amount of whitespace `\s` to be in front of the citation.
