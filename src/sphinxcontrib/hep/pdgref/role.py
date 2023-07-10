"""Link to PDG reviews and listings in Sphinx documentation."""

from typing import Dict, List, Optional, Tuple

from docutils import nodes
from docutils.nodes import Node, system_message
from docutils.parsers.rst.states import Inliner
from sphinx.util.typing import RoleFunction

from .entry import PDGEntry
from .url import URLPattern, create_link_text, create_url


def pdgref(pattern: URLPattern) -> RoleFunction:
    def role(  # noqa: PLR0913
        name: str,
        rawtext: str,
        text: str,
        lineno: int,
        inliner: Inliner,
        options: Optional[Dict] = None,
        content: Optional[List[str]] = None,
    ) -> Tuple[List[Node], List[system_message]]:
        try:
            pdg_entry = PDGEntry.from_str(text)
            link_text = create_link_text(pdg_entry, pattern=pattern)
            url = create_url(pdg_entry, pattern=pattern)
        except ValueError as e:
            msg = (
                f"Badly formatted argument:\n  {rawtext}\nThis role requires at most 3"
                " semicolon-separated arguments: section; [year; [page number(s)]]"
                ' with page numbers something like "p12", or "pp. 12-15, 17". The'
                " order does not matter"
            )
            raise ValueError(msg) from e
        if options is None:
            options = {}
        # cspell:ignore refuri
        node = nodes.reference(rawtext, link_text, refuri=url, **options)
        return [node], []

    return role
