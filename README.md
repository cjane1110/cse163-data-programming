# CSE 163 Data Programming Portfolio

Hsichen (Olivia) Chang

This portfolio presents selected work completed for CSE 163, with an emphasis
on Python programming, data analysis, testing, visualization, and clear
technical documentation.

## Selected projects

| Project | Focus | Demonstrated skills |
| --- | --- | --- |
| [Python Foundations](01-python-foundations/) | Small data-processing functions and a creative analysis notebook | Python control flow, collections, descriptive statistics, text normalization, and assert-based testing |
| [Social Network Analysis](02-network-analysis/) | Friendship graphs, recommendation strategies, and graph visualization | NetworkX graph modeling, traversal, ranking, deterministic output, Matplotlib, and `unittest` |
| [Pokemon Data Analysis](03-pokemon-data-analysis/) | Parallel manual and pandas implementations of the same analysis interface | pandas, filtering, aggregation, missing-data handling, interface consistency, and comparative testing |

## Setup

After cloning or downloading this repository, open a terminal in the repository
root and create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

On Windows PowerShell, activate the environment with:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

To open any of the creative analysis notebooks, start Jupyter from the
repository root:

```bash
jupyter notebook
```

## Run and test the projects

Run each command from the repository root with the virtual environment active.

### Python Foundations

```bash
cd 01-python-foundations
python3 hw1_test.py
```

### Social Network Analysis

```bash
cd 02-network-analysis
python3 network_analysis.py
MPLBACKEND=Agg python3 network_graphs.py
python3 -m unittest -v test_network_analysis.py
```

`MPLBACKEND=Agg` allows the graph images to be generated in a terminal or
other headless environment.

### Pokemon Data Analysis

```bash
cd 03-pokemon-data-analysis
python3 test_pokemon.py
```

Each project directory includes a README with further implementation and
analysis details.

## Coursework disclosure

This repository contains a selected portfolio of completed coursework. It is
shared to demonstrate the author's learning and technical work; it is not a
complete archive of the course.
