"""Link to PDG reviews and listings in Sphinx documentation."""

from typing import Any, Dict
from warnings import warn

from sphinx.application import Sphinx

from .role import URLPattern, pdgref

warn(
    (
        "The sphinxcontrib.hep.pdgref package is deprecated. Please install the"
        " [sphinx-hep-pdgref](https://pypi.org/project/sphinx-hep-pdgref) package and"
        " import `sphinx_hep_pdg` instead."
    ),
    category=DeprecationWarning,
    stacklevel=2,
)


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_role("pdg-listing", role=pdgref(pattern=URLPattern.LISTING))
    app.add_role("pdg-review", role=pdgref(pattern=URLPattern.REVIEW))
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
