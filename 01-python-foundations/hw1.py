"""
hw1.py

Author: Hsichen (Olivia) Chang
Date: 2026-04-09

This file contains functions for basic data processing and analysis.
The functions work with numerical data and text, including computing
statistics and organizing data into useful formats.

Functions:
- total(n): returns the sum of numbers from 0 to n
- median(numbers): returns the median of a sorted list
- five_number_summary(numbers): returns min, Q1, median, Q3, max
- num_outliers(numbers): counts values outside the IQR range
- text_normalize(text): removes non-letter characters and converts text to
  lowercase

These functions demonstrate the use of loops, conditionals, and data
structures such as lists, tuples, and sets.
"""


def total(n):
    """
    Returns the sum of the numbers from 0 to n (inclusive).
    If n is negative, returns None.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def median(numbers):
    """
    Given a sorted list of numbers, returns the median.
    """
    n = len(numbers)

    result = None
    if len(numbers) % 2 == 1:
        result = numbers[n // 2]
    else:
        upper_num = numbers[n // 2]
        lower_num = numbers[n // 2 - 1]
        result = (upper_num + lower_num) / 2

    return result


def five_number_summary(numbers):
    """
    Given a sorted list of numbers, returns a tuple of the five-number
    summary: the minimum, first quartile, median, third quartile,
    and maximum. For a singleton list, all five values are that number.
    """
    n = len(numbers)

    if n == 1:
        return (numbers[0],) * 5

    if n % 2 == 0:
        lower_half = numbers[:n // 2]
        upper_half = numbers[n // 2:]
    else:
        lower_half = numbers[:n // 2]
        upper_half = numbers[n // 2 + 1:]

    return (
        numbers[0],
        median(lower_half),
        median(numbers),
        median(upper_half),
        numbers[-1],
    )


def num_outliers(numbers):
    summary = five_number_summary(numbers)
    Q1 = summary[1]
    Q3 = summary[3]

    interquartile_range = Q3 - Q1
    lowerbound = Q1 - 1.5 * interquartile_range
    upperbound = Q3 + 1.5 * interquartile_range

    count = 0
    for num in numbers:
        if num < lowerbound or num > upperbound:
            count += 1

    return count


def text_normalize(text):
    result = ""

    for char in text:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            result += char.lower()

    return result
