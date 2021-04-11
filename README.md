# PDG role for Sphinx

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
:pdg-review:`Kinematics`

:pdg-review:`2014; Resonances`

:pdg-review:`Resonances; 2018; pp. 2-4, 7`

:pdg-review:`QCD; p5`

:pdg-listing:`QCD; p5`

:pdg-review:`QCD; p5`
```

which will render in the HTML pages as:

> [PDG2020, §Kinematics](https://pdg.lbl.gov/2020/reviews/rpp2020-rev-kinematics.pdf)
>
> [PDG2014, §Resonances](https://pdg.lbl.gov/2014/reviews/rpp2014-rev-resonances.pdf)
>
> [PDG2018, §Resonances, pp.2-4,7](https://pdg.lbl.gov/2018/reviews/rpp2018-rev-resonances.pdf#page=2)
>
> [PDG2020, §QCD, p.5](https://pdg.lbl.gov/2020/reviews/rpp2020-rev-qcd.pdf#page=5)
>
> [PDG2020, §QCD, p.5](https://pdg.lbl.gov/2020/reviews/rpp2020-rev-qcd.pdf#page=5)
>
> [PDG2018](https://pdg.lbl.gov/2018/listings/rpp2018-list-K-zero.pdf)

_Note that the resulting links lead to the correct page as well!_
