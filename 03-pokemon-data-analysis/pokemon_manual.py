"""
Name: Hsichen (Olivia) Chang
Section: CSE 163 A
Description:
Manual Pokemon data analysis using basic Python collections rather than
DataFrame operations.
"""

from __future__ import annotations

from cse163_utils import Pokemon, parse


class PokemonManual:
    """Process and analyze Pokemon data with lists and dictionaries."""

    def __init__(self, filepath: str) -> None:
        """Read the CSV data and store it as Pokemon dictionaries."""
        self._data: list[Pokemon] = parse(filepath)

    def species_count(self) -> int:
        """Return the number of unique Pokemon species."""
        species = set()

        for pokemon in self._data:
            species.add(pokemon["name"])

        return len(species)

    def max_level(self) -> tuple[str, int]:
        """Return the name and level of the highest-level Pokemon."""
        max_pokemon = self._data[0]

        for pokemon in self._data:
            if pokemon["level"] > max_pokemon["level"]:
                max_pokemon = pokemon

        return (max_pokemon["name"], max_pokemon["level"])

    def filter_range(self, lower: int, upper: int) -> list[str]:
        """Return names with levels in the half-open range [lower, upper)."""
        names = []

        for pokemon in self._data:
            if lower <= pokemon["level"] < upper:
                names.append(pokemon["name"])

        return names

    def mean_attack_for_type(self, poke_type: str) -> float | None:
        """Return the mean attack for a type, or None when it is absent."""
        total = 0
        count = 0

        for pokemon in self._data:
            attack = pokemon["atk"]
            if pokemon["type"] == poke_type and attack == attack:
                total += attack
                count += 1

        if count == 0:
            return None

        return total / count
