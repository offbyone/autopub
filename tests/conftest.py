import os
import shutil
from pathlib import Path
from typing import Any, Generator

import pytest


VALID_RELEASE_TEXT = """
---
release type: patch
---

This is a new release.
"""

MISSING_RELEASE_NOTES_TEXT = """
---
release type: patch
---
"""

DEPRECATED_RELEASE_TEXT = """
Release type: patch

This is a new release.
"""


@pytest.fixture
def valid_release_text() -> str:
    return VALID_RELEASE_TEXT.strip()


@pytest.fixture
def missing_release_notes_text() -> str:
    return MISSING_RELEASE_NOTES_TEXT.strip()


@pytest.fixture
def deprecated_release_text() -> str:
    return DEPRECATED_RELEASE_TEXT.strip()


@pytest.fixture
def temporary_working_directory(tmpdir: Any) -> Generator[Path, None, None]:
    with tmpdir.as_cwd():
        yield Path(tmpdir)


@pytest.fixture
def example_project() -> Generator[Path, None, None]:
    # TODO: make a copy of this

    project_path = Path(__file__).parent / "fixtures/example-project"

    shutil.rmtree(project_path / "dist", ignore_errors=True)

    current_working_directory = os.getcwd()

    os.chdir(project_path)

    try:
        yield project_path
    finally:
        os.chdir(current_working_directory)
