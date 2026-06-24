"""
Name: Hsichen (Olivia) Chang
Section: CSE 163 A
Description:
Shared data types and CSV parsing utilities for the Pokemon analysis.
"""

from typing import TypedDict

import pandas as pd


TOLERANCE = 0.001

Pokemon = TypedDict(
    "Pokemon",
    {
        "id": int,
        "name": str,
        "level": int,
        "personality": str,
        "type": str,
        "weakness": str,
        "atk": int,
        "def": int,
        "hp": int,
        "stage": int,
    },
)


def parse(file_name: str) -> list[Pokemon]:
    """
    Read a Pokemon CSV file as a list containing one dictionary per row.
    """
    data = pd.read_csv(file_name)
    return data.to_dict("records")
