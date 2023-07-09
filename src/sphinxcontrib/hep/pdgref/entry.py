"""Data formatters for generating a link to a review or listing in the PDG.

As an example, the `PDG <https://pdg.lbl.gov>`_ has its pdf files for reviews
stored as:

.. code-block::

    https://pdg.lbl.gov/2020/reviews/rpp2020-rev-resonances.pdf#page=3

Note the page number. This is `a trick
<https://helpx.adobe.com/acrobat/kb/link-html-pdf-page-acrobat.html>_` to
directly lead to the correct page number when clicking the generated link.
"""

import re
from typing import Optional

from attrs import field, frozen

DEFAULT_YEAR = 2020


@frozen
class PDGEntry:
    """Data container for a link as described in `format`."""

    section: str
    year: int
    pages: Optional[str]
    first_page: Optional[int] = field(init=False, repr=False)

    def __attrs_post_init__(self) -> None:
        if self.pages is None:
            first_page = None
        else:
            first_page = get_first_page(self.pages)
        object.__setattr__(self, "first_page", first_page)

    @staticmethod
    def from_str(text: str) -> "PDGEntry":
        """Create an entry from the contents of the :code:`pdg` role.

        >>> from sphinxcontrib.hep.pdgref.entry import PDGEntry
        >>> PDGEntry.from_str("Resonances; 2018; p.5")
        PDGEntry(section='Resonances', year=2018, pages='5')
        >>> PDGEntry.from_str("Resonances")
        PDGEntry(section='Resonances', year=2020, pages=None)
        """
        segments = text.split(";")
        if len(segments) > 3:  # noqa: PLR2004
            msg = f'Input string "{text}" contains more than 3 segments'
            raise ValueError(msg)
        section = text
        year = DEFAULT_YEAR
        pages = None
        for segment in text.split(";"):
            year_ = get_year(segment)
            if year_ is not None:
                year = year_
                continue
            pages_ = get_page_numbers(segment)
            if pages_ is not None:
                pages = pages_
                continue
            section = segment.strip()
        return PDGEntry(section, year, pages)


def get_first_page(text: str) -> int:
    text = text.strip()
    matches = re.match(r"p?p?\.?\s*(\d+).*", text)
    if matches is None:
        msg = f'Badly formatted page numbers "{text}"'
        raise ValueError(msg)
    first_page_nr = matches.group(1)
    return int(first_page_nr)


def get_page_numbers(text: str) -> Optional[str]:
    text = text.strip()
    matches = re.match(r"pp?\.?\s*(\d+.*)", text)
    if matches is None:
        return None
    page_nr_def = matches.group(1)
    return page_nr_def.replace(" ", "")


def get_year(text: str) -> Optional[int]:
    text = text.strip()
    matches = re.match(r"\d{4}", text)
    if matches is None:
        return None
    year_def = matches.group(0)
    return int(year_def)
