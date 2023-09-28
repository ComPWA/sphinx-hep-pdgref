# PDG role for Sphinx

[![PyPI package](https://badge.fury.io/py/sphinx-hep-pdgref.svg)](https://pypi.org/project/sphinx-hep-pdgref)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/sphinx-hep-pdgref)](https://pypi.org/project/sphinx-hep-pdgref)
[![BSD 3-Clause license](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Open in Visual Studio Code](https://img.shields.io/badge/vscode-open-blue?logo=visualstudiocode)](https://open.vscode.dev/ComPWA/sphinx-hep-pdgref)
[![GitPod](https://img.shields.io/badge/gitpod-open-blue?logo=gitpod)](https://gitpod.io/#https://github.com/ComPWA/sphinx-hep-pdgref)
[![Test coverage](https://codecov.io/gh/ComPWA/sphinx-hep-pdgref/branch/main/graph/badge.svg?token=SS8ZB8J11N)](https://codecov.io/gh/ComPWA/sphinx-hep-pdgref)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/dbe042deb2914f6098eb98586d3983fe)](https://www.codacy.com/gh/ComPWA/sphinx-hep-pdgref)
[![CI status](https://github.com/ComPWA/sphinx-hep-pdgref/workflows/CI-tests/badge.svg)](https://github.com/ComPWA/sphinx-hep-pdgref/actions?query=branch%3Amain+workflow%3ACI-tests)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy.readthedocs.io)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ComPWA/sphinx-hep-pdgref/main.svg)](https://results.pre-commit.ci/latest/github/ComPWA/sphinx-hep-pdgref/main)
[![Spelling checked](https://img.shields.io/badge/cspell-checked-brightgreen.svg)](https://github.com/streetsidesoftware/cspell/tree/master/packages/cspell)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

This package is a
[Sphinx extension](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)
that makes it easy to refer to PDF files of reviews and particle listings in the PDG.

## Installation

Just install through [PyPI](https://pypi.org) with `pip`:

```bash
pip install sphinx-hep-pdgref
```

Next, in your
[Sphinx configuration file](https://www.sphinx-doc.org/en/master/usage/configuration.html)
(`conf.py`), add `"sphinx_hep_pdgref"` to your `extensions`:

```python
extensions = [
    # ...
    "sphinx_hep_pdgref",
    # ...
]
```

## Usage

There are two roles, one for the
[particle listings](https://pdg.lbl.gov/2020/listings/contents_listings.html) and one
for the [review](https://pdg.lbl.gov/2020/reviews/contents_sports.html). These roles can
be used as follows:

```restructuredtext
:pdg-listing:`K-zero`

:pdg-review:`Kinematics`

:pdg-review:`2014; Resonances`

:pdg-review:`Resonances; 2018; pp. 2-4, 7`

:pdg-review:`QCD; p5`

:pdg-review:`PDG2015; Quark Model; p.2`
```

which will render in the HTML pages as:

> [PDG2020](https://pdg.lbl.gov/2020/listings/rpp2020-list-K-zero.pdf)
>
> [PDG2020, §Kinematics](https://pdg.lbl.gov/2020/reviews/rpp2020-rev-kinematics.pdf)
>
> [PDG2014, §Resonances](https://pdg.lbl.gov/2014/reviews/rpp2014-rev-resonances.pdf)
>
> [PDG2018, §Resonances, pp.2-4,7](https://pdg.lbl.gov/2018/reviews/rpp2018-rev-resonances.pdf#page=2)
>
> [PDG2020, §QCD, p.5](https://pdg.lbl.gov/2020/reviews/rpp2020-rev-qcd.pdf#page=5)
>
> [PDG2015, §Quark Model, p.2](https://pdg.lbl.gov/2015/reviews/rpp2015-rev-qcd.pdf#page=2)

_Note that the resulting links lead to the correct page as well!_
