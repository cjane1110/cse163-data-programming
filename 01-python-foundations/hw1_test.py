"""
hw1_test.py

Author: Hsichen (Olivia) Chang
Date: 2026-04-09

This file contains test functions for the functions implemented in hw1.py.
Each test function uses assert statements to verify the correctness of
the corresponding function, including total, median, five_number_summary,
num_outliers, and text_normalize.

These tests help ensure that the functions handle both typical cases and
edge cases correctly.
"""

import hw1


def test_total():
    """
    Tests the total method
    """
    assert (15 == hw1.total(5))
    assert (21 == hw1.total(6))
    assert (10 == hw1.total(4))
    assert (None == hw1.total(-3))


def test_median():
    assert 3 == hw1.median([1, 2, 3, 4, 5])
    assert 2.5 == hw1.median([1, 2, 3, 4])
    assert 14 == hw1.median([12, 13, 14, 15, 16])


def test_five_number_summary():
    assert (7, 7, 7, 7, 7) == hw1.five_number_summary([7])
    assert (1, 1.5, 3, 4.5, 5) == hw1.five_number_summary([1, 2, 3, 4, 5])
    assert (1, 1, 1, 1, 1) == hw1.five_number_summary([1, 1, 1, 1, 1])
    assert (30, 31, 36, 45, 53) == hw1.five_number_summary(
        [30, 31, 31, 34, 36, 38, 39, 51, 53]
    )
    assert (5, 13, 15, 17, 25) == hw1.five_number_summary(
        [5, 13, 14, 15, 16, 17, 25]
    )
    assert (5, 12.5, 15.5, 27.5, 30) == hw1.five_number_summary(
        [5, 12, 12, 13, 13, 15, 16, 26, 26, 29, 29, 30]
    )
    assert (12, 13, 15.5, 26, 29) == hw1.five_number_summary(
        [12, 12, 13, 13, 15, 16, 26, 26, 29, 29]
    )
    assert (2, 2.5, 4, 5.5, 6) == hw1.five_number_summary([2, 3, 4, 5, 6])
    assert (10, 12.5, 20, 27.5, 30) == hw1.five_number_summary(
        [10, 15, 20, 25, 30]
    )


def test_num_outliers():
    assert 0 == hw1.num_outliers([7])
    assert 0 == hw1.num_outliers([1, 2, 3, 4, 5])
    assert 0 == hw1.num_outliers([1, 99, 200, 500, 506, 507])
    assert 2 == hw1.num_outliers([5, 13, 14, 15, 16, 17, 25])
    assert 2 == hw1.num_outliers([33, 34, 35, 36, 36, 36, 37, 37, 100, 101])
    assert 1 == hw1.num_outliers([8, 11, 11, 11, 11, 11])
    assert 0 == hw1.num_outliers([10, 11, 12, 13, 14])
    assert 0 == hw1.num_outliers([1, 2, 3, 4, 5, 100, 200])


def test_text_normalize():
    assert "hello" == hw1.text_normalize("Hello")
    assert "hello" == hw1.text_normalize("Hello!")
    assert "hellother" == hw1.text_normalize("heLLo tHEr3!!!")
    assert "" == hw1.text_normalize("123!!!")
    assert "abcxyz" == hw1.text_normalize("ABC xyz")


def main():
    test_total()
    test_median()
    test_five_number_summary()
    test_num_outliers()
    test_text_normalize()
    print("passed")


if __name__ == '__main__':
    main()
