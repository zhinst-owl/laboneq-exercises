# LabOne Q exercises

Short, self-contained notebooks to practise [LabOne Q](https://docs.zhinst.com/labone_q_user_manual/).
All of them run in emulation: no instrument is needed.

## Exercises

🔎 **[Exercise finder](https://zhinst-owl.github.io/laboneq-exercises/)** – filter by level, type and topic.

<!-- index:start -->
| # | Exercise | Level | Topics | Type |
| --- | --- | --- | --- | --- |
| 005 | [Long flux pulse on one SHFQC](exercises/005_long_flux_pulse/exercise.ipynb) ([solution](exercises/005_long_flux_pulse/solution.ipynb)) | basic | `Gen2`, `SHFQC`, `flux`, `calibration`, `pulses`, `markers`, `sweeps` | write-the-code |
| 004 | [Chirp pulse sweep](exercises/004_chirp_pulse_sweep/exercise.ipynb) ([solution](exercises/004_chirp_pulse_sweep/solution.ipynb)) | basic | `Gen2`, `dsl`, `pulses`, `sweeps`, `chunking` | write-the-code |
| 001 | [Hahn echo timing](exercises/001_hahn_echo_timing/exercise.ipynb) ([solution](exercises/001_hahn_echo_timing/solution.ipynb)) | medium | `dsl`, `sections`, `timing`, `Gen2` | fix-the-bugs |
| 003 | [Readout amplitude sweep](exercises/003_readout_amplitude_sweep/exercise.ipynb) ([solution](exercises/003_readout_amplitude_sweep/solution.ipynb)) | medium | `Gen2`, `SHFQA`, `readout`, `sweeps`, `chunking` | fix-the-bugs |
| 002 | [Four frequencies on one output](exercises/002_output_router/exercise.ipynb) ([solution](exercises/002_output_router/solution.ipynb)) | advanced | `Gen2`, `SHFSG`, `output-router`, `calibration`, `device-setup` | fix-the-bugs |
<!-- index:end -->

The exercises are listed from the easiest to the hardest, so you can do them from top to bottom.
The number of an exercise is only its identifier and never changes.

Each exercise lives in its own folder with two notebooks:

- `exercise.ipynb` – the task
- `solution.ipynb` – the solved notebook with a short explanation

## Tags

Every exercise has one **level**, one **type** and one or more **topics**.
They are shown at the top of the notebook and in the table above.

| Level | Meaning |
| --- | --- |
| `basic` | First steps: write a simple experiment from start to end |
| `medium` | You know the LabOne Q basics and have run a few experiments |
| `advanced` | You write your own experiments and workflows |
| `expert` | Corner cases, hardware limits, real support cases |

| Type | Meaning |
| --- | --- |
| `write-the-code` | Fill in the missing code |
| `fix-the-bugs` | The notebook looks complete, but fails or gives the wrong result |
| `quiz` | Questions to answer, little or no code to write |

Topics in use: `Gen2`, `dsl`, `sections`, `timing`, `pulses`, `sweeps`, `chunking`, `readout`, `calibration`, `device-setup`, `SHFSG`, `SHFQA`, `SHFQC`, `flux`, `markers`, `output-router`.
Planned: `workflow`, `automation`, `phase`, `feedback`, `applications-library`, `openqasm`, `ZQCS`.

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[test]"
jupyter lab
```

## Add an exercise

See [CONTRIBUTING.md](CONTRIBUTING.md).
