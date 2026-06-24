# Python Foundations

Author: Hsichen (Olivia) Chang

This project demonstrates introductory Python techniques through small
data-processing functions and a creative analysis notebook.

## Statistical analysis

The five-number summary describes a sorted numeric dataset with its minimum,
first quartile (Q1), median, third quartile (Q3), and maximum. The quartiles
summarize the lower and upper halves of the data, while the median marks its
center.

Outlier detection uses the interquartile range, `IQR = Q3 - Q1`. Values below
`Q1 - 1.5 * IQR` or above `Q3 + 1.5 * IQR` are counted as outliers.

## Text normalization

`text_normalize` scans a string character by character, keeps only ASCII
letters, converts them to lowercase, and joins them without spaces or
punctuation. For example, `"heLLo tHEr3!!!"` becomes `"hellother"`.

## Python fundamentals

The project demonstrates functions, loops, conditionals, ranges, string
operations, list slicing, tuples, dictionaries, indexing, accumulation, and
assert-based testing. The creative notebook extends these ideas with date
formatting and coordinate-pair construction.

## Run the tests

First enter the project folder:

```bash
cd 01-python-foundations
```

Then run:

```bash
python3 hw1_test.py
```
