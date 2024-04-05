"""Link to PDG reviews and listings in Sphinx documentation."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .role import URLPattern, pdgref

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_role("pdg-listing", role=pdgref(pattern=URLPattern.LISTING))
    app.add_role("pdg-review", role=pdgref(pattern=URLPattern.REVIEW))
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
