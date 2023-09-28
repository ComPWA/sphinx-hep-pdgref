import sys

import pytest

if sys.version_info < (3, 8):
    from importlib_metadata import version
else:
    from importlib.metadata import version

pytest_plugins = "sphinx.testing.fixtures"
collect_ignore = ["roots"]


# cspell:ignore rootdir
sphinx_version = version("Sphinx")
if sphinx_version < "7.2":
    from sphinx.testing.path import path

    @pytest.fixture(scope="session")
    def rootdir() -> path:
        return path(__file__).parent.abspath() / "roots"

else:
    from pathlib import Path

    @pytest.fixture(scope="session")
    def rootdir() -> Path:
        return Path(__file__).parent.absolute() / "roots"
