"""Link to PDG reviews and listings in Sphinx documentation."""

from typing import Any, Dict

from sphinx.application import Sphinx

from .role import URLPattern, pdgref


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_role("pdg-listing", role=pdgref(pattern=URLPattern.LISTING))
    app.add_role("pdg-review", role=pdgref(pattern=URLPattern.REVIEW))
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
