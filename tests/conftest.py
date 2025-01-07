from importlib.metadata import version

import pytest

pytest_plugins = "sphinx.testing.fixtures"
collect_ignore = ["roots"]


# cspell:ignore rootdir
sphinx_version = version("Sphinx")
if sphinx_version < "7.2":
    from sphinx.testing.path import path

    @pytest.fixture(scope="session")
    def rootdir() -> path:  # pyright:ignore[reportRedeclaration]
        return path(__file__).parent.abspath() / "roots"

else:
    from pathlib import Path

    @pytest.fixture(scope="session")  # type:ignore[misc]
    def rootdir() -> Path:
        return Path(__file__).parent.absolute() / "roots"
