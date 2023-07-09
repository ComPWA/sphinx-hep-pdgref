import pytest

from sphinxcontrib.hep.pdgref.entry import DEFAULT_YEAR, PDGEntry  # type:ignore[import]
from sphinxcontrib.hep.pdgref.url import (  # type:ignore[import]
    URLPattern,
    create_link_text,
    create_url,
)


@pytest.mark.parametrize(
    ("entry", "link_text", "url"),
    [
        (
            PDGEntry.from_str("Resonances; 2018; p. 3"),
            "PDG2018, §Resonances, p.3",
            "https://pdg.lbl.gov/2018/reviews/rpp2018-rev-resonances.pdf#page=3",
        ),
        (
            PDGEntry.from_str("Resonances; 2016; p2-5"),
            "PDG2016, §Resonances, pp.2-5",
            "https://pdg.lbl.gov/2016/reviews/rpp2016-rev-resonances.pdf#page=2",
        ),
        (
            PDGEntry.from_str("2019; QCD"),
            "PDG2019, §QCD",
            "https://pdg.lbl.gov/2019/reviews/rpp2019-rev-qcd.pdf",
        ),
        (
            PDGEntry.from_str("Kinematics"),
            f"PDG{DEFAULT_YEAR}, §Kinematics",
            f"https://pdg.lbl.gov/{DEFAULT_YEAR}/reviews/rpp{DEFAULT_YEAR}-rev-kinematics.pdf",
        ),
        (
            PDGEntry.from_str("K-zero"),
            f"PDG{DEFAULT_YEAR}",
            f"https://pdg.lbl.gov/{DEFAULT_YEAR}/listings/rpp{DEFAULT_YEAR}-list-K-zero.pdf",
        ),
        (
            PDGEntry.from_str("K-zero; 2018; p.4"),
            "PDG2018",
            "https://pdg.lbl.gov/2018/listings/rpp2018-list-K-zero.pdf#page=4",
        ),
        (
            PDGEntry.from_str("2012; pi-plus-minus"),
            "PDG2012",
            "https://pdg.lbl.gov/2012/listings/rpp2012-list-pi-plus-minus.pdf",
        ),
        (PDGEntry.from_str("pi+ pi-"), None, None),
    ],
)
def test_create_link_text_url(entry: PDGEntry, link_text: str, url: str):
    if link_text is None or url is None:  # pyright: ignore[reportUnnecessaryComparison]
        with pytest.raises(ValueError, match=r"^URL cannot contain spaces or commas$"):
            create_url(entry, pattern=URLPattern.LISTING)
        return
    if "listings" in url:
        assert create_link_text(entry, pattern=URLPattern.LISTING) == link_text
        assert create_url(entry, pattern=URLPattern.LISTING) == url
    elif "reviews" in url:
        assert create_link_text(entry, pattern=URLPattern.REVIEW) == link_text
        assert create_url(entry, pattern=URLPattern.REVIEW) == url
    else:
        raise NotImplementedError
