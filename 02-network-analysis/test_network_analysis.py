import contextlib
import io
import tempfile
import unittest
from importlib import import_module
from pathlib import Path

import networkx as nx

try:
    network_analysis = import_module("network_analysis")
except ModuleNotFoundError:
    network_analysis = None

try:
    network_graphs = import_module("network_graphs")
except ModuleNotFoundError:
    network_graphs = None


class NetworkAnalysisTest(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = nx.Graph()
        self.graph.add_edges_from(
            [
                (0, 1),
                (0, 2),
                (1, 3),
                (1, 4),
                (2, 3),
                (2, 5),
            ]
        )

    def test_read_network_adds_edges_and_ignores_comments(self) -> None:
        self.assertIsNotNone(network_analysis)
        graph = nx.Graph()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "links.txt"
            path.write_text(
                "# Authored example network\n"
                "\n"
                "10 20\n"
                "20 30 optional-column\n",
                encoding="utf-8",
            )
            network_analysis.read_network(graph, path)

        self.assertEqual({10, 20, 30}, set(graph.nodes))
        self.assertEqual({(10, 20), (20, 30)}, set(graph.edges))

    def test_included_network_is_nontrivial_connected_synthetic_graph(self) -> None:
        self.assertIsNotNone(network_analysis)
        self.assertEqual(
            "synthetic-social-network.txt",
            network_analysis.SYNTHETIC_NETWORK_PATH.name,
        )

        graph = nx.Graph()
        network_analysis.read_network(
            graph,
            network_analysis.SYNTHETIC_NETWORK_PATH,
        )

        self.assertGreaterEqual(graph.number_of_nodes(), 30)
        self.assertGreaterEqual(graph.number_of_edges(), 60)
        self.assertTrue(nx.is_connected(graph))
        self.assertTrue(
            all(
                network_analysis.recs_by_common_friends(graph, user)
                for user in network_analysis.DEMO_USERS
            )
        )

    def test_main_prints_each_representative_demo_user(self) -> None:
        self.assertIsNotNone(network_analysis)
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            network_analysis.main()

        rendered = output.getvalue()
        for user in network_analysis.DEMO_USERS:
            self.assertIn(f"{user} (by num_common_friends):", rendered)
            self.assertIn(f"{user} (by influence):", rendered)

    def test_friends_of_friends_excludes_user_and_existing_friends(self) -> None:
        self.assertIsNotNone(network_analysis)
        self.assertEqual({3, 4, 5}, network_analysis.friends_of_friends(self.graph, 0))

    def test_common_friend_recommendations_sort_by_score_then_user_id(self) -> None:
        self.assertIsNotNone(network_analysis)
        self.assertEqual(
            [3, 4, 5],
            network_analysis.recs_by_common_friends(self.graph, 0),
        )

    def test_influence_recommendations_weight_less_connected_friends_more(self) -> None:
        self.assertIsNotNone(network_analysis)
        graph = nx.Graph()
        graph.add_edges_from(
            [
                (0, 1),
                (0, 2),
                (1, 3),
                (1, 5),
                (1, 6),
                (2, 4),
            ]
        )

        recommendations = network_analysis.recs_by_influence(graph, 0)

        self.assertLess(recommendations.index(4), recommendations.index(3))


class NetworkGraphsTest(unittest.TestCase):
    def test_graph_layout_is_deterministic(self) -> None:
        self.assertIsNotNone(network_graphs)
        graph = network_graphs.get_practice_graph()

        first = network_graphs.get_layout(graph)
        second = network_graphs.get_layout(graph)

        self.assertEqual(set(first), set(second))
        for node in graph:
            self.assertEqual(first[node].tolist(), second[node].tolist())

    def test_practice_graph_has_expected_nodes_and_edges(self) -> None:
        self.assertIsNotNone(network_graphs)
        graph = network_graphs.get_practice_graph()

        self.assertEqual(set("ABCDEF"), set(graph.nodes))
        self.assertEqual(8, graph.number_of_edges())

    def test_practice_digraph_preserves_edge_direction(self) -> None:
        self.assertIsNotNone(network_graphs)
        graph = network_graphs.get_practice_digraph()

        self.assertTrue(graph.has_edge(1, 2))
        self.assertFalse(graph.has_edge(2, 1))
        self.assertEqual(8, graph.number_of_nodes())


if __name__ == "__main__":
    unittest.main()
