"""Friend recommendation algorithms for a synthetic undirected social network.

Author: Hsichen (Olivia) Chang
"""

from __future__ import annotations

from pathlib import Path

import networkx as nx


SYNTHETIC_NETWORK_PATH = Path(__file__).with_name(
    "synthetic-social-network.txt"
)
DEMO_USERS = (0, 12, 24, 30)


def read_network(graph: nx.Graph, filename: str | Path) -> None:
    """Add each non-comment edge in ``filename`` to ``graph``."""
    with open(filename, encoding="utf-8") as links:
        for row in links:
            stripped = row.strip()
            if not stripped or stripped.startswith("#"):
                continue
            person1, person2, *_ = stripped.split()
            graph.add_edge(int(person1), int(person2))


def friends(graph: nx.Graph, user: int) -> set[int]:
    """Return the users directly connected to ``user``."""
    return set(graph.neighbors(user))


def friends_of_friends(graph: nx.Graph, user: int) -> set[int]:
    """Return non-friends reachable from ``user`` by exactly two edges."""
    user_friends = friends(graph, user)
    candidates = set()
    for friend in user_friends:
        candidates |= friends(graph, friend)
    return candidates - user_friends - {user}


def common_friends(graph: nx.Graph, user1: int, user2: int) -> set[int]:
    """Return the direct friends shared by ``user1`` and ``user2``."""
    return friends(graph, user1) & friends(graph, user2)


def recs_by_common_friends(graph: nx.Graph, user: int) -> list[int]:
    """Rank friend-of-friend candidates by shared-friend count."""
    scores = {
        person: len(common_friends(graph, user, person))
        for person in friends_of_friends(graph, user)
    }
    return sorted(scores, key=lambda person: (-scores[person], person))


def recs_by_influence(graph: nx.Graph, user: int) -> list[int]:
    """Rank candidates by the inverse degree of each shared friend."""
    scores = {}
    for person in friends_of_friends(graph, user):
        scores[person] = sum(
            1 / len(friends(graph, friend))
            for friend in common_friends(graph, user, person)
        )
    return sorted(scores, key=lambda person: (-scores[person], person))


def main() -> None:
    """Print recommendations for representative synthetic-network nodes."""
    graph = nx.Graph()
    read_network(graph, SYNTHETIC_NETWORK_PATH)

    print("Synthetic network recommendations by common friends:")
    print()
    for user in DEMO_USERS:
        recommendations = recs_by_common_friends(graph, user)[:10]
        print(user, "(by num_common_friends):", recommendations)

    different_count = 0
    print()
    print("Recommendations by influence:")
    print()
    for user in DEMO_USERS:
        common_recommendations = recs_by_common_friends(graph, user)[:10]
        influence_recommendations = recs_by_influence(graph, user)[:10]
        if common_recommendations != influence_recommendations:
            different_count += 1
        print(user, "(by influence):", influence_recommendations)

    print()
    print("Demo users with different rankings:", different_count)


if __name__ == "__main__":
    main()
