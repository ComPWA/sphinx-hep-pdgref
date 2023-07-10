from typing import Optional

import pytest

from sphinxcontrib.hep.pdgref.entry import (
    DEFAULT_YEAR,
    PDGEntry,
    get_first_page,
    get_page_numbers,
    get_year,
)


class TestPDGEntry:
    @pytest.mark.parametrize(
        ("text", "expected", "first_page"),
        [
            (
                "2018; Resonances; pp. 2-4, 6",
                PDGEntry(year=2018, section="Resonances", pages="2-4,6"),
                2,
            ),
            (
                "kinematics",
                PDGEntry(year=DEFAULT_YEAR, section="kinematics", pages=None),
                None,
            ),
            (  # four entries is bad
                "PDG; 2018; Resonances; pp.2-5",
                None,
                None,
            ),
        ],
    )
    def test_from_str(
        self,
        text: str,
        expected: Optional[PDGEntry],
        first_page: Optional[int],
    ):
        if expected is None:
            with pytest.raises(
                ValueError,
                match=r'Input string ".+" contains more than 3 segments',
            ):
                entry = PDGEntry.from_str(text)
        else:
            entry = PDGEntry.from_str(text)
            assert entry == expected
            assert entry.first_page == first_page
            from_eval = eval(str(entry))  # noqa: S307
            assert entry == from_eval


@pytest.mark.parametrize(
    ("text", "formatted_pages", "first_page"),
    [
        ("test", None, None),
        ("5", None, 5),
        ("7-9", None, 7),
        ("p5", "5", 5),
        (" p5", "5", 5),
        ("p.5 ", "5", 5),
        ("pp. 2-4, 6", "2-4,6", 2),
        ("pp. 5-7, 9 ", "5-7,9", 5),
        ("\tp1,3", "1,3", 1),
    ],
)
def test_get_page_numbers(
    text: str, formatted_pages: Optional[str], first_page: Optional[int]
):
    assert get_page_numbers(text) == formatted_pages
    if first_page is None:
        with pytest.raises(
            ValueError, match=rf'Badly formatted page numbers "{text}"'
        ) as exception:
            get_first_page(text)
        assert text in str(exception.value)
    else:
        assert get_first_page(text) == first_page


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("1993", 1993),
        ("\t1993 ", 1993),
        ("2021", 2021),
        ("2021 ", 2021),
        ("753", None),
        ("(2021)", None),
        (" '12", None),
        ("p. 12-15", None),
    ],
)
def test_get_year(text: str, expected: Optional[int]):
    assert get_year(text) == expected
