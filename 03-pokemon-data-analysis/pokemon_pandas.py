"""
Name: Hsichen (Olivia) Chang
Section: CSE 163 A
Description:
Pokemon data analysis implemented with pandas DataFrame operations.
"""

from __future__ import annotations

import pandas as pd


class PokemonPandas:
    """Process and analyze Pokemon data with pandas."""

    def __init__(self, filepath: str) -> None:
        """Read the CSV data into a DataFrame."""
        self._data: pd.DataFrame = pd.read_csv(filepath)

    def species_count(self) -> int:
        """Return the number of unique Pokemon species."""
        return len(self._data["name"].unique())

    def max_level(self) -> tuple[str, int]:
        """Return the name and level of the highest-level Pokemon."""
        max_row = self._data.loc[self._data["level"].idxmax()]
        return (max_row["name"], max_row["level"])

    def filter_range(self, lower: int, upper: int) -> list[str]:
        """Return names with levels in the half-open range [lower, upper)."""
        filtered = self._data[
            (self._data["level"] >= lower) & (self._data["level"] < upper)
        ]

        return list(filtered["name"])

    def mean_attack_for_type(self, poke_type: str) -> float | None:
        """Return the mean attack for a type, or None when it is absent."""
        attacks = self._data.loc[self._data["type"] == poke_type, "atk"]

        mean_attack = attacks.mean()
        if pd.isna(mean_attack):
            return None

        return mean_attack
