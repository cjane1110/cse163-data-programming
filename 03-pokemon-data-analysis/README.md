# Pokemon Data Analysis

Author: Hsichen (Olivia) Chang

This project implements the same Pokemon-analysis interface in two ways. The
manual version uses Python lists, dictionaries, loops, sets, and accumulators
to analyze parsed row dictionaries. Its shared parsing utility uses pandas to
read the CSV file. The pandas version works directly with a `DataFrame` and
expresses the same questions with column selection, boolean filters, and
aggregation methods.

## Analysis features

Both `PokemonManual` and `PokemonPandas` support:

- counting unique Pokemon species;
- finding the highest-level Pokemon;
- filtering Pokemon within a half-open level range;
- aggregating attack values by Pokemon type; and
- returning `None` when an aggregation has no matching type.

The shared method names and return values make the implementations directly
comparable. This same-interface, two-implementations design demonstrates how
Python loops and data structures can perform the same analysis as pandas
DataFrame operations, even though both implementations rely on pandas at the
file-reading layer.

## Missing-data analysis

`creative-analysis.ipynb` explores `pokemon_missing.csv`, which contains gaps
in several stat columns. The notebook fills each missing attack from its own
Pokemon type's mean when that type has valid attack data; otherwise, the value
remains missing. This analysis shows how pandas filtering and aggregation can
support a documented, data-informed imputation without changing complete
columns such as HP.

## Setup

From the repository root, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pandas jupyter
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Run the tests

Change into the project folder and run the assert-based test suite:

```bash
cd 03-pokemon-data-analysis
python3 test_pokemon.py
```

To explore the missing-data analysis interactively, start Jupyter and open
`creative-analysis.ipynb`:

```bash
jupyter notebook
```
