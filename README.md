# LabOne Q exercises

Short, self-contained notebooks to practise [LabOne Q](https://docs.zhinst.com/labone_q_user_manual/).
All of them run in emulation: no instrument is needed.

## Exercises

🔎 **[Exercise finder](https://zhinst-owl.github.io/laboneq-exercises/)** – filter by level, type and topic.

<!-- index:start -->
| # | Exercise | Level | Topics | Type |
| --- | --- | --- | --- | --- |
| 110 | [Long flux pulse on one SHFQC](exercises/110_long_flux_pulse/exercise.ipynb) ([solution](exercises/110_long_flux_pulse/solution.ipynb)) | basic | `Gen2`, `SHFQC`, `flux`, `calibration`, `pulses`, `markers`, `sweeps` | write-the-code |
| 120 | [Chirp pulse sweep](exercises/120_chirp_pulse_sweep/exercise.ipynb) ([solution](exercises/120_chirp_pulse_sweep/solution.ipynb)) | basic | `Gen2`, `dsl`, `pulses`, `sweeps`, `chunking` | write-the-code |
| 130 | [Fix the environment](exercises/130_fix_the_environment/exercise.ipynb) ([solution](exercises/130_fix_the_environment/solution.ipynb)) | basic | `environment`, `installation`, `applications-library`, `HDAWG`, `flux` | fix-the-bugs |
| 210 | [Hahn echo timing](exercises/210_hahn_echo_timing/exercise.ipynb) ([solution](exercises/210_hahn_echo_timing/solution.ipynb)) | medium | `dsl`, `sections`, `timing`, `Gen2` | fix-the-bugs |
| 220 | [Readout amplitude sweep](exercises/220_readout_amplitude_sweep/exercise.ipynb) ([solution](exercises/220_readout_amplitude_sweep/solution.ipynb)) | medium | `Gen2`, `SHFQA`, `readout`, `sweeps`, `chunking` | fix-the-bugs |
| 230 | [e-f Rabi on a shared drive port](exercises/230_ef_rabi_shared_port/exercise.ipynb) ([solution](exercises/230_ef_rabi_shared_port/solution.ipynb)) | medium | `Gen2`, `SHFQC`, `dsl`, `sections`, `timing`, `calibration`, `sweeps` | write-the-code |
| 310 | [Four frequencies on one output](exercises/310_output_router/exercise.ipynb) ([solution](exercises/310_output_router/solution.ipynb)) | advanced | `Gen2`, `SHFSG`, `output-router`, `calibration`, `device-setup` | fix-the-bugs |
| 320 | [e-f Rabi as a workflow](exercises/320_ef_rabi_workflow/exercise.ipynb) ([solution](exercises/320_ef_rabi_workflow/solution.ipynb)) | advanced | `Gen2`, `SHFQC`, `workflow`, `quantum-operations`, `applications-library`, `sweeps` | write-the-code |
| 330 | [Find the qubit: widening the search window](exercises/330_peak_search_automation/exercise.ipynb) ([solution](exercises/330_peak_search_automation/solution.ipynb)) | advanced | `automation`, `workflow`, `applications-library`, `spectroscopy`, `sweeps` | write-the-code |
<!-- index:end -->

The exercises are listed from the easiest to the hardest, so you can do them from top to bottom.
The folder numbers follow the same order: the first digit is the level (`1` basic, `2` medium, `3` advanced, `4` expert), the other two digits the position inside the level. Numbers are spaced by 10, so new exercises fit in between and existing numbers never change.

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

Topics in use: `Gen2`, `dsl`, `sections`, `timing`, `pulses`, `sweeps`, `chunking`, `readout`, `calibration`, `device-setup`, `SHFSG`, `SHFQA`, `SHFQC`, `HDAWG`, `flux`, `markers`, `output-router`, `workflow`, `quantum-operations`, `applications-library`, `automation`, `spectroscopy`, `environment`, `installation`.
Planned: `phase`, `feedback`, `openqasm`, `ZQCS`.

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[test]"
jupyter lab
```

## Add an exercise

See [CONTRIBUTING.md](CONTRIBUTING.md).
