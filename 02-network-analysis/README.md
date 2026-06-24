# Social Network Analysis

Author: Hsichen (Olivia) Chang

This project models connections in a synthetic social network as an undirected
NetworkX graph and compares two friend-recommendation strategies. The included
network is entirely synthetic, was authored for this portfolio, and contains
no real user data. It also includes small graph visualizations and a creative
course-prerequisite network.

## How the analysis works

`network_analysis.py` reads each data row of
`synthetic-social-network.txt` and uses the first two integer node IDs as an
undirected edge. Comment lines beginning with `#` document the dataset and are
ignored by the loader. The graph contains three densely connected communities
plus a set of bridge nodes, providing enough structure to compare recommendation
rankings across different neighborhoods.

For a selected user, the friends-of-friends traversal visits every direct
friend, gathers that friend's neighbors, and removes the selected user and
existing friends. The remaining nodes are recommendation candidates.

The two ranking methods are:

- **Common-friend scoring:** counts the intersection of the user's friends and
  each candidate's friends.
- **Influence scoring:** gives each shared friend a weight of
  `1 / number_of_friends`. A connection through a less-connected person
  therefore contributes more than one through a highly connected person.

Both methods sort by descending score, then ascending user ID. This secondary
sort makes tied recommendations deterministic across runs. The command-line
demo prints results for four fixed nodes selected from different parts of the
synthetic graph.

## Visualization

`network_graphs.py` constructs one undirected example graph and one directed
example graph, then renders them with NetworkX and Matplotlib. A fixed seed
makes the spring layouts reproducible, while explicit figure, node, label, and
arrow sizing keeps both diagrams legible. Running it creates
`practice_graph.png` and `practice_digraph.png`. These generated images are
intentionally ignored rather than stored in the portfolio.

`creative-analysis.ipynb` is a separate, manually authored educational example
that extends `nx.DiGraph` into a `CourseNetwork`. Directed edges point from
illustrative prerequisites to the courses that depend on them, supporting
queries in both directions as well as course-attribute lookup. It does not use
external social-network or user data.

## Setup

From the repository root, create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

With the environment active, install the dependencies:

```bash
python -m pip install networkx matplotlib
```

## Run

Change into `02-network-analysis`, keeping the virtual environment active:

```bash
cd 02-network-analysis
python network_analysis.py
python network_graphs.py
python -m unittest -v test_network_analysis.py
```

For graph generation in a terminal or other headless environment, use:

```bash
MPLBACKEND=Agg python network_graphs.py
```
