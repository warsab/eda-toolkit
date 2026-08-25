"""
name_matching.py
~~~~~~~~~~~~~~~~

Utility functions for detecting duplicate name pairs in a Pandas DataFrame.

Dependencies
------------
- pandas
- rapidfuzz[fuzzywuzzy]   # or fuzzywuzzy>=0.18

Example
-------
>>> import pandas as pd
>>> from eda_toolkit.name_matching import find_exact_name_duplicates
>>>
>>> df = pd.DataFrame({
...     "FirstName": ["Norman", "norman", "Alice", "Bob"],
...     "Surname":   ["Smith",  "Smith",  "Jones", "Brown"]
... })
>>>
>>> dupes = find_exact_name_duplicates(df)
>>> dupes
  FirstName Surname  Count
0    Norman   Smith      2
"""
from __future__ import annotations

import pandas as pd
from typing import List, Tuple

# --------------------------------------------------------------------------- #
# Exact-match utility                                                         #
# --------------------------------------------------------------------------- #
def find_exact_name_duplicates(
    df: pd.DataFrame,
    first_name_col: str = "FirstName",
    surname_col: str = "Surname",
    min_count: int = 2,
    sort_desc: bool = True,
) -> pd.DataFrame:
    """
    Return rows where *(first_name, surname)* occurs `min_count` times or more.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing at least first- and surname columns.
    first_name_col : str, default "FirstName"
        Column name holding the first / given names.
    surname_col : str, default "Surname"
        Column name holding the surnames.
    min_count : int, default 2
        Minimum duplicate threshold to include in output.
    sort_desc : bool, default True
        Sort result by the duplicate count in descending order.

    Returns
    -------
    pd.DataFrame
        A DataFrame with columns  ``[first_name_col, surname_col, "Count"]``.
    """
    dupes = (
        df.groupby([first_name_col, surname_col], dropna=False)
        .size()
        .reset_index(name="Count")
    )
    dupes = dupes[dupes["Count"] >= min_count]

    if sort_desc:
        dupes = dupes.sort_values(by="Count", ascending=False)

    return dupes


# --------------------------------------------------------------------------- #
# Fuzzy-match utility                                                         #
# --------------------------------------------------------------------------- #
def find_fuzzy_name_duplicates(
    df: pd.DataFrame,
    first_name_col: str = "FirstName",
    surname_col: str = "Surname",
    score_cutoff: int = 90,
) -> List[Tuple[str, str, str, str, int]]:
    """
    Identify *approximate* duplicates using a token-sort ratio on full name.

    Returns a list of tuples:
        (first_name_a, surname_a, first_name_b, surname_b, similarity_score)

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the names to compare.
    first_name_col : str, default "FirstName"
        Column name holding the first / given names.
    surname_col : str, default "Surname"
        Column name holding the surnames.
    score_cutoff : int, default 90
        Minimum similarity (0-100) to consider a fuzzy match.

    Notes
    -----
    - Uses *rapidfuzz* if available (faster); falls back to *fuzzywuzzy*.
    - Runtime is *O(n²)* for n records; consider pre-filtering large sets.
    """
    try:
        from rapidfuzz import fuzz  # type: ignore
    except ImportError:
        from fuzzywuzzy import fuzz  # noqa: F401

    names = df[[first_name_col, surname_col]].astype(str)
    full_names = (names[first_name_col] + " " + names[surname_col]).tolist()

    matches: List[Tuple[str, str, str, str, int]] = []
    for i in range(len(full_names)):
        for j in range(i + 1, len(full_names)):
            score = fuzz.token_sort_ratio(full_names[i], full_names[j])
            if score >= score_cutoff:
                fn_a, sn_a = names.iloc[i]
                fn_b, sn_b = names.iloc[j]
                matches.append((fn_a, sn_a, fn_b, sn_b, score))
    return matches
