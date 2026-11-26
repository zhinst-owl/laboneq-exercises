"""Rebuild the exercise table in README.md from the notebook tags.

Run from the repository root:

    python tools/update_index.py
"""

from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
START = "<!-- index:start -->"
END = "<!-- index:end -->"

LEVELS = ["basic", "medium", "advanced", "expert"]
TYPES = ["write-the-code", "fix-the-bugs", "quiz"]


def read_tags(folder):
    """Return the tags stored in the metadata of exercise.ipynb."""
    notebook = nbformat.read(folder / "exercise.ipynb", as_version=4)
    return notebook.metadata["exercise"]


def build_table():
    lines = [
        "| # | Exercise | Level | Topics | Type |",
        "| --- | --- | --- | --- | --- |",
    ]
    for folder in sorted((ROOT / "exercises").iterdir()):
        if not (folder / "exercise.ipynb").exists():
            continue
        tags = read_tags(folder)
        link = f"exercises/{folder.name}"
        topics = ", ".join(f"`{topic}`" for topic in tags["topics"])
        lines.append(
            f"| {tags['id']} | [{tags['title']}]({link}/exercise.ipynb) "
            f"([solution]({link}/solution.ipynb)) "
            f"| {tags['level']} | {topics} | {tags['type']} |"
        )
    return "\n".join(lines)


def updated_readme():
    text = README.read_text()
    before = text.split(START)[0]
    after = text.split(END)[1]
    return before + START + "\n" + build_table() + "\n" + END + after


if __name__ == "__main__":
    README.write_text(updated_readme())
    print("README.md index updated")
