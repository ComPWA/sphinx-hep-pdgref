"""Create an URL to a PDF file in the PDG.

The URL is formatted in such a way that it leads to a page number if available,
`like so
<https://helpx.adobe.com/acrobat/kb/link-html-pdf-page-acrobat.html>`_.
"""

import re
from enum import Enum

from .entry import PDGEntry


class URLPattern(str, Enum):
    LISTING = "https://pdg.lbl.gov/{0}/listings/rpp{0}-list-{1}.pdf"
    REVIEW = "https://pdg.lbl.gov/{0}/reviews/rpp{0}-rev-{1}.pdf"


def create_url(entry: PDGEntry, *, pattern: URLPattern) -> str:
    if pattern == URLPattern.LISTING:
        url = _create_listing_url(entry)
    elif pattern == URLPattern.REVIEW:
        url = _create_review_url(entry)
    else:
        msg = f"No implementation for {pattern}"
        raise NotImplementedError(msg)
    if " " in url or "," in url:
        msg = "URL cannot contain spaces or commas"
        raise ValueError(msg)
    return url


def _create_listing_url(entry: PDGEntry) -> str:
    url = URLPattern.LISTING.format(entry.year, entry.section)  # type: ignore[str-format]
    url += __create_page_anchor(entry)
    return url


def _create_review_url(entry: PDGEntry) -> str:
    section_url = entry.section
    section_url = section_url.lower()
    section_url = section_url.replace(" ", "-")
    url = URLPattern.REVIEW.format(entry.year, section_url)  # type: ignore[str-format]
    url += __create_page_anchor(entry)
    return url


def __create_page_anchor(entry: PDGEntry) -> str:
    if entry.first_page is not None:
        return f"#page={entry.first_page}"
    return ""


def create_link_text(entry: PDGEntry, *, pattern: URLPattern) -> str:
    if pattern == URLPattern.LISTING:
        return _create_short_link_text(entry)
    if pattern == URLPattern.REVIEW:
        return _create_extended_link_text(entry)
    msg = f"No implementation for {pattern}"
    raise NotImplementedError(msg)


def _create_extended_link_text(entry: PDGEntry) -> str:
    label = f"PDG{entry.year}, §{entry.section}"
    if entry.pages is not None:
        if re.match(r"^\d+$", entry.pages):
            label += f", p.{entry.pages}"
        else:
            label += f", pp.{entry.pages}"
    return label


def _create_short_link_text(entry: PDGEntry) -> str:
    return f"PDG{entry.year}"
