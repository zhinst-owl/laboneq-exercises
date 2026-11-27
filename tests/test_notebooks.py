"""Run every exercise and solution notebook in emulation.

- solution.ipynb must run without any error.
- exercise.ipynb may fail only in cells tagged ``raises-exception``,
  and each of those cells must really fail (so the bugs stay bugs
  when LabOne Q is upgraded).
- The tags and the README index must be consistent.

Run with:

    pip install -e ".[test]"
    pytest
"""

import sys
from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import update_index  # noqa: E402

FOLDERS = update_index.exercise_folders()
IDS = [folder.name for folder in FOLDERS]


def run_notebook(path):
    notebook = nbformat.read(path, as_version=4)
    client = NotebookClient(
        notebook,
        timeout=600,
        kernel_name="python3",
        resources={"metadata": {"path": str(path.parent)}},
    )
    client.execute()
    return notebook


def has_error(cell):
    return any(output.output_type == "error" for output in cell.get("outputs", []))


@pytest.mark.parametrize("folder", FOLDERS, ids=IDS)
def test_tags(folder):
    tags = update_index.read_tags(folder)
    assert folder.name.startswith(tags["id"] + "_")
    assert tags["level"] in update_index.LEVELS
    # The first digit of the number is the level: 1 basic, 2 medium, ...
    assert len(tags["id"]) == 3
    assert int(tags["id"][0]) == update_index.LEVELS.index(tags["level"]) + 1
    assert tags["type"] in update_index.TYPES
    assert len(tags["topics"]) > 0
    solution = nbformat.read(folder / "solution.ipynb", as_version=4)
    assert solution.metadata["exercise"] == tags


@pytest.mark.parametrize("folder", FOLDERS, ids=IDS)
def test_solution_runs(folder):
    notebook = run_notebook(folder / "solution.ipynb")
    for cell in notebook.cells:
        assert "raises-exception" not in cell.metadata.get("tags", [])


@pytest.mark.parametrize("folder", FOLDERS, ids=IDS)
def test_exercise_fails_only_where_expected(folder):
    notebook = run_notebook(folder / "exercise.ipynb")
    for cell in notebook.cells:
        if "raises-exception" in cell.metadata.get("tags", []):
            assert has_error(cell), "cell is tagged raises-exception but ran fine"


def test_readme_index_is_up_to_date():
    assert update_index.README.read_text() == update_index.updated_readme()


def test_finder_page_is_up_to_date():
    assert update_index.FINDER.read_text() == update_index.updated_finder()
