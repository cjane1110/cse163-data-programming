"""
Name: Hsichen (Olivia) Chang
Section: CSE 163 A
Description:
Tests for the manual and pandas implementations of the Pokemon data analysis
interface.
"""

from pokemon_manual import PokemonManual
from pokemon_pandas import PokemonPandas


SPEC_TEST_FILE = "pokemon_test.csv"
MISSING_TEST_FILE = "pokemon_missing.csv"


def test_species_count(
    manual_analyzer: PokemonManual, pandas_analyzer: PokemonPandas
) -> None:
    """Both implementations count unique Pokemon species."""
    expected = 3

    assert manual_analyzer.species_count() == expected
    assert pandas_analyzer.species_count() == expected


def test_max_level(
    manual_analyzer: PokemonManual, pandas_analyzer: PokemonPandas
) -> None:
    """Both implementations return the highest-level Pokemon."""
    expected = ("Lapras", 72)

    assert manual_analyzer.max_level() == expected
    assert pandas_analyzer.max_level() == expected


def test_filter_range(
    manual_analyzer: PokemonManual, pandas_analyzer: PokemonPandas
) -> None:
    """Both implementations include the lower bound and exclude the upper."""
    expected = ["Arcanine", "Arcanine", "Starmie"]

    assert manual_analyzer.filter_range(35, 72) == expected
    assert pandas_analyzer.filter_range(35, 72) == expected


def test_mean_attack_for_type(
    manual_analyzer: PokemonManual, pandas_analyzer: PokemonPandas
) -> None:
    """Both implementations average attacks for a requested Pokemon type."""
    expected = 47.5

    assert manual_analyzer.mean_attack_for_type("fire") == expected
    assert pandas_analyzer.mean_attack_for_type("fire") == expected


def test_missing_type(
    manual_analyzer: PokemonManual, pandas_analyzer: PokemonPandas
) -> None:
    """Both implementations return None when a type is absent."""
    assert manual_analyzer.mean_attack_for_type("grass") is None
    assert pandas_analyzer.mean_attack_for_type("grass") is None


def test_mean_attack_skips_missing_values(
    manual_analyzer: PokemonManual, pandas_analyzer: PokemonPandas
) -> None:
    """Both implementations exclude missing attacks from a type mean."""
    expected = 54.2

    assert manual_analyzer.mean_attack_for_type("dragon") == expected
    assert pandas_analyzer.mean_attack_for_type("dragon") == expected


def test_mean_attack_with_no_valid_values(
    manual_analyzer: PokemonManual, pandas_analyzer: PokemonPandas
) -> None:
    """Both implementations return None when all attacks are missing."""
    assert manual_analyzer.mean_attack_for_type("flying") is None
    assert pandas_analyzer.mean_attack_for_type("flying") is None


def main() -> None:
    manual_analyzer = PokemonManual(SPEC_TEST_FILE)
    pandas_analyzer = PokemonPandas(SPEC_TEST_FILE)
    missing_manual_analyzer = PokemonManual(MISSING_TEST_FILE)
    missing_pandas_analyzer = PokemonPandas(MISSING_TEST_FILE)

    test_species_count(manual_analyzer, pandas_analyzer)
    test_max_level(manual_analyzer, pandas_analyzer)
    test_filter_range(manual_analyzer, pandas_analyzer)
    test_mean_attack_for_type(manual_analyzer, pandas_analyzer)
    test_missing_type(manual_analyzer, pandas_analyzer)
    test_mean_attack_skips_missing_values(
        missing_manual_analyzer, missing_pandas_analyzer
    )
    test_mean_attack_with_no_valid_values(
        missing_manual_analyzer, missing_pandas_analyzer
    )


if __name__ == "__main__":
    main()
