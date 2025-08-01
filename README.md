# ug_xtdc4

HTML/PDF User Guide for the cronologic **xTDC4** time-to-digital converter.

This is a Sphinx project that creates the User Guide for the
[xTDC4](https://www.cronologic.de/product/xtdc4), time-to-digital converter
(TDC) from [cronologic GmbH & Co. KG](https://www.cronologic.de).

Find the documentation online at
[docs.cronologic.de/xtdc4](https://docs.cronologic.de/xtdc4).

## Prerequisites

Python is necessary for creating the HTML output.

Python and LuaLaTeX are necessary for creating the LaTeX/PDF output.

Optionally, create and activate a virtual environment

```shell
python -m venv .venv
. .\.venv\Scripts\activate
```

Depending on your operating system, you may need to run a different activation script.

The requirements are listed in `requirements.txt`, `requirements-frozen.txt`, and
`requirements-dev.txt`.

If you want to guarantee the output to be the same as hosted at
[docs.cronologic.de/xtdc4](https://docs.cronologic.de/xtdc4), install the
packages listed in `requirements-frozen.txt`, that is, run

```shell
pip install -r requirements-frozen.txt
```

If you want to install the most up-to-date versions of the prerequisites, use
`requirements.txt`.

If you want to install the most up-to-date versions and also install plotting libraries
(e.g., to run Python scripts in [\_figures/](source/_figures/)), use
`requirements-dev.txt`.

### Fonts for LaTeX

The `fontspec` package is used for the LaTeX output. It may complain that fonts are
missing from your system.

The following fonts are required for the LaTeX output and are included in the listed
packages.

- Montserrat (main font): [montserrat](https://ctan.org/tex-archive/fonts/montserrat)
- TeX Gyre Adventor (headings font): [tex-gyre](https://ctan.org/pkg/tex-gyre)
- Latin Modern Math (math font): [lm-math](https://ctan.org/pkg/lm-math)
- Latin Modern Mono Light (monospaced font): [lm](https://ctan.org/pkg/lm)
- KerkisSans (expanded Greek letters): [kerkis](https://ctan.org/pkg/kerkis)

## Building

Run

```shell
make html
```

or

```shell
make latexpdf
```

to compile the project as HTML or PDF. The HTML (PDF) output is in `build/html/`
(`build/latex/`).

## License

![Creative Commons by-nd 4.0](https://i.creativecommons.org/l/by-nd/4.0/88x31.png)

This documentation is licensed under the
[CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/) license. You are free to
copy and redistribute the material in any medium or format for any purpose, even
commercially unchanged if you give appropriate credit to cronologic GmbH & Co. KG. A
link to [this repository](https://github.com/cronologic-de/ug_timetagger4) or the
[product page](https://www.cronologic.de/product/timetagger) is sufficient. If you
decide to contribute to this repository, you transfer non-exclusive but unlimited rights
to your edit to cronologic GmbH & Co. KG.

The file [extraplaceins.sty](extraplaceins.sty) is in the public domain.
