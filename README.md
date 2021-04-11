# PDG role for Sphinx

[![PyPI package](https://badge.fury.io/py/sphinxcontrib-hep-pdgref.svg)](https://pypi.org/project/sphinxcontrib-hep-pdgref)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/sphinxcontrib-hep-pdgref)](https://pypi.org/project/sphinxcontrib-hep-pdgref)
[![GPLv3+ license](https://img.shields.io/badge/License-GPLv3+-blue.svg)](https://www.gnu.org/licenses/gpl-3.0-standalone.html)
[![Test coverage](https://codecov.io/gh/ComPWA/sphinxcontrib-hep-pdgref/branch/main/graph/badge.svg?token=SS8ZB8J11N)](https://codecov.io/gh/ComPWA/sphinxcontrib-hep-pdgref)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/dbe042deb2914f6098eb98586d3983fe)](https://www.codacy.com/gh/ComPWA/sphinxcontrib-hep-pdgref)
[![CI status](https://github.com/ComPWA/sphinxcontrib-hep-pdgref/workflows/CI-tests/badge.svg)](https://github.com/ComPWA/sphinxcontrib-hep-pdgref/actions?query=branch%3Amain+workflow%3ACI-tests)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy.readthedocs.io)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen)](https://github.com/pre-commit/pre-commit)
[![Prettier](https://camo.githubusercontent.com/687a8ae8d15f9409617d2cc5a30292a884f6813a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64655f7374796c652d70726574746965722d6666363962342e7376673f7374796c653d666c61742d737175617265)](https://prettier.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort)

This package is a
[Sphinx extension](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)
that makes it easy to refer to PDF files of reviews and particle listings in
the PDG.

## Installation

Just install through [PyPI](https://pypi.org) with `pip`:

```bash
pip install sphinxcontrib-hep-pdgref
```

Next, in your
[Sphinx configuration file](https://www.sphinx-doc.org/en/master/usage/configuration.html)
(`conf.py`), add `"sphinxcontrib.hep.pdgref"` to your `extensions`:

```python
extensions = [
    ...
    "sphinxcontrib.hep.pdgref",
    ...
]
```

## Usage

There are two roles, one for the
[particle listings](https://pdg.lbl.gov/2020/listings/contents_listings.html)
and one for the
[review](https://pdg.lbl.gov/2020/reviews/contents_sports.html). These roles
can be used as follows:

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
