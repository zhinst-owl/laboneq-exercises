"""Rebuild the exercise table in README.md and the exercise finder page
(docs/index.html) from the notebook tags.

Run from the repository root:

    python tools/update_index.py
"""

import json
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
START = "<!-- index:start -->"
END = "<!-- index:end -->"

FINDER = ROOT / "docs" / "index.html"
FINDER_TEMPLATE = ROOT / "tools" / "finder_template.html"
REPOSITORY = "https://github.com/zhinst-owl/laboneq-exercises"

LEVELS = ["basic", "medium", "advanced", "expert"]
TYPES = ["write-the-code", "fix-the-bugs", "quiz"]


def read_tags(folder):
    """Return the tags stored in the metadata of exercise.ipynb."""
    notebook = nbformat.read(folder / "exercise.ipynb", as_version=4)
    return notebook.metadata["exercise"]


def difficulty(folder):
    """Sorting key: the exercise number. Its first digit is the level
    (1 basic, 2 medium, 3 advanced, 4 expert), so the numbers follow the difficulty."""
    return read_tags(folder)["id"]


def exercise_folders():
    """Return the exercise folders, ordered from the easiest to the hardest."""
    folders = []
    for folder in (ROOT / "exercises").iterdir():
        if (folder / "exercise.ipynb").exists():
            folders.append(folder)
    return sorted(folders, key=difficulty)


def build_table():
    lines = [
        "| # | Exercise | Level | Topics | Type |",
        "| --- | --- | --- | --- | --- |",
    ]
    for folder in exercise_folders():
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


def updated_finder():
    """Return the finder page: the template with the exercise tags filled in."""
    exercises = []
    topics = []
    for folder in exercise_folders():
        tags = read_tags(folder)
        link = f"{REPOSITORY}/blob/main/exercises/{folder.name}"
        exercises.append(
            {
                "id": tags["id"],
                "title": tags["title"],
                "level": tags["level"],
                "type": tags["type"],
                "topics": tags["topics"],
                "exercise_url": f"{link}/exercise.ipynb",
                "solution_url": f"{link}/solution.ipynb",
            }
        )
        for topic in tags["topics"]:
            if topic not in topics:
                topics.append(topic)
    data = {
        "repository": REPOSITORY,
        "levels": LEVELS,
        "types": TYPES,
        "topics": sorted(topics, key=str.lower),
        "exercises": exercises,
    }
    return FINDER_TEMPLATE.read_text().replace("/*DATA*/", json.dumps(data, indent=1))


if __name__ == "__main__":
    README.write_text(updated_readme())
    FINDER.parent.mkdir(exist_ok=True)
    FINDER.write_text(updated_finder())
    print("README.md and docs/index.html updated")
