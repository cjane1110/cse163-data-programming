"""Create example undirected and directed network visualizations.

Author: Hsichen (Olivia) Chang
"""

import matplotlib.pyplot as plt
import networkx as nx


LAYOUT_SEED = 163


def get_layout(graph: nx.Graph) -> dict:
    """Return reproducible spring-layout coordinates for a graph."""
    return nx.spring_layout(graph, seed=LAYOUT_SEED, k=5.0, iterations=500)


def get_practice_graph() -> nx.Graph:
    """Return a small undirected graph used to demonstrate connectivity."""
    graph = nx.Graph()
    graph.add_nodes_from(["A", "B", "C", "D", "E", "F"])
    graph.add_edges_from(
        [
            ("A", "B"),
            ("A", "C"),
            ("B", "C"),
            ("B", "D"),
            ("C", "D"),
            ("C", "F"),
            ("D", "E"),
            ("D", "F"),
        ]
    )
    return graph


def get_practice_digraph() -> nx.DiGraph:
    """Return a small directed graph with one disconnected component."""
    graph = nx.DiGraph()
    graph.add_nodes_from(range(1, 9))
    graph.add_edges_from(
        [
            (1, 2),
            (1, 3),
            (2, 3),
            (3, 4),
            (3, 8),
            (6, 7),
        ]
    )
    return graph


def main() -> None:
    """Render both example graphs as PNG images."""
    practice_graph = get_practice_graph()
    figure, axis = plt.subplots(figsize=(8, 6))
    nx.draw_networkx(
        practice_graph,
        pos=get_layout(practice_graph),
        ax=axis,
        node_size=1200,
        font_size=12,
        width=1.5,
    )
    axis.margins(0.15)
    axis.set_axis_off()
    figure.tight_layout()
    figure.savefig("practice_graph.png", dpi=150)
    plt.close(figure)

    practice_digraph = get_practice_digraph()
    figure, axis = plt.subplots(figsize=(9, 6))
    nx.draw_networkx(
        practice_digraph,
        pos=get_layout(practice_digraph),
        ax=axis,
        node_size=1200,
        font_size=12,
        width=1.5,
        arrows=True,
        arrowsize=24,
        connectionstyle="arc3,rad=0.05",
    )
    axis.margins(0.18)
    axis.set_axis_off()
    figure.tight_layout()
    figure.savefig("practice_digraph.png", dpi=150)
    plt.close(figure)


if __name__ == "__main__":
    main()
