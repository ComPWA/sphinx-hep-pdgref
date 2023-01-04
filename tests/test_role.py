import pyquery as pq  # pyright: ignore[reportMissingTypeStubs]
import pytest

from sphinxcontrib.hep.pdgref.entry import DEFAULT_YEAR  # type:ignore[import]


@pytest.mark.sphinx("text", testroot="dummy")
def test_text(app, warning) -> None:
    app.build()
    assert not warning.getvalue()
    output = (app.outdir / "index.txt").read_text()
    lines = output.split("\n")
    assert lines[::2] == [
        f"PDG{DEFAULT_YEAR}",
        "PDG2018",
        "PDG2015, §Quark Model, p.2",
        f"PDG{DEFAULT_YEAR}, §Kinematics",
        f"PDG{DEFAULT_YEAR}, §QCD, p.5",
        "PDG2014, §Resonances",
        "PDG2018, §Resonances, pp.12-14,17",
    ]


@pytest.mark.sphinx("html", testroot="dummy")
def test_html(app, warning) -> None:
    app.build()
    assert not warning.getvalue()
    html_str = (app.outdir / "index.html").read_text()
    html = pq.PyQuery(html_str)
    external_refs = html.find("a").filter(".reference")
    assert [ref.text for ref in external_refs] == [
        f"PDG{DEFAULT_YEAR}",
        "PDG2018",
        "PDG2015, §Quark Model, p.2",
        "PDG2020, §Kinematics",
        "PDG2020, §QCD, p.5",
        "PDG2014, §Resonances",
        "PDG2018, §Resonances, pp.12-14,17",
    ]
    assert [ref.get("href") for ref in external_refs] == [
        "https://pdg.lbl.gov/2020/listings/rpp2020-list-K-zero.pdf",
        "https://pdg.lbl.gov/2018/listings/rpp2018-list-pi-plus-minus.pdf",
        "https://pdg.lbl.gov/2015/reviews/rpp2015-rev-quark-model.pdf#page=2",
        "https://pdg.lbl.gov/2020/reviews/rpp2020-rev-kinematics.pdf",
        "https://pdg.lbl.gov/2020/reviews/rpp2020-rev-qcd.pdf#page=5",
        "https://pdg.lbl.gov/2014/reviews/rpp2014-rev-resonances.pdf",
        "https://pdg.lbl.gov/2018/reviews/rpp2018-rev-resonances.pdf#page=12",
    ]


def href(text: str) -> str:
    return text
