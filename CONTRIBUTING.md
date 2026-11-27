# Adding an exercise

1. Copy an existing folder to `exercises/<NNN>_<short_name>/` (next free number).
2. Edit `exercise.ipynb` and `solution.ipynb`.
3. Set the tags in **both** notebooks (see below).
4. Run `python tools/update_index.py` to refresh the table in the README and the finder page (`docs/index.html`).
5. Run `pytest`.

## Tags

The tags are stored in the notebook metadata
(Jupyter Lab: *Property Inspector → Advanced Tools → Notebook metadata*):

```json
"exercise": {
    "id": "001",
    "title": "Hahn echo timing",
    "level": "medium",
    "topics": ["dsl", "sections", "timing", "Gen2"],
    "type": "fix-the-bugs",
    "source": "LabOne Q Quiz"
}
```

- `level`: `basic`, `medium`, `advanced` or `expert`
- `order` (optional): position inside the level, lower comes first. Without it (default 100) exercises of the same level are sorted by number.
- `type`: `write-the-code`, `fix-the-bugs` or `quiz`
- `topics`: free list, reuse the existing ones when possible
- `source`: where the idea comes from (quiz, support case, ...). **No customer names or case details.**

Repeat level, topics and type in the first cell of the notebook so they are visible when reading.

## Style rules

- **Self-contained.** Each notebook builds its own device setup, calibration and session. No imports from other exercises. Importing from `laboneq` and `laboneq_applications` is fine.
- **Emulation only.** `session.connect(do_emulation=True)`.
- **Simple Python.** Plain loops and functions. Avoid comprehensions inside comprehensions, `*args` tricks, lambdas, classes.
- **Short text.** A few lines per cell. Let the code and the questions do the work.
- **Link the manual.** Every section (device setup, calibration, session, ...) links to the matching page of the [user manual](https://docs.zhinst.com/labone_q_user_manual/), even if another exercise already has the same link.
- **Hints** go in collapsed `<details>` blocks.
- **Same structure** in exercise and solution, so they can be compared side by side.

## Exercises with bugs

For `fix-the-bugs` exercises:

- Tag every cell that fails in the notebook as shipped with the cell tag `raises-exception`.
  The tests check that these cells really fail, so we notice when a LabOne Q upgrade makes a bug disappear.
- Silent bugs (wrong result, no error) need a check the reader can run, for example a plot with the expected result written next to it.
- `solution.ipynb` must run without any error.
