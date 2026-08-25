<div align="center">

# 🔍 eda-toolkit

### *Stop rewriting the same first ten cells.*

A small Python helper library for **exploratory data analysis in notebooks**.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/python/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](https://opensource.org/licenses/MIT)

<sub>Works in **Jupyter** · **VS Code** · **Microsoft Fabric** · **Databricks**</sub>

</div>

---

When you first open an unfamiliar dataset you end up writing the same cells over and
over — check what's missing, style a table so it's readable, plot a correlation
matrix, hunt for outliers, find near-duplicate records. `eda-toolkit` wraps those into
one-line calls so the notebook stays focused on the analysis instead of the
boilerplate.

Built on **pandas** and **Plotly**.

---

## ⚡ Installation

```bash
git clone https://github.com/warsab/eda-toolkit.git
cd eda-toolkit
pip install -e .
```

Optional extras:

```bash
pip install -e ".[fuzzy]"     # rapidfuzz, for fuzzy name matching
pip install -e ".[parquet]"   # pyarrow, to read .parquet files
pip install -e ".[all]"       # everything, incl. the example notebook
```

Or just copy the `eda_toolkit/` folder into your project and import it directly.

---

## 📦 Modules

| Module | What it does |
|---|---|
| `diagnostics` | Missing-value summary: count, percentage, and dtype per column, rendered as a Plotly table |
| `visualization` | Correlation heatmap, scatter plots with OLS trendlines, and an outlier box-plot explorer with a feature slider |
| `styling` | Styled DataFrame previews — captions, highlighted min/max, heatmaps, and inline bars |
| `extractors` | Pull numeric values out of messy text columns |
| `name_matching` | Find exact and fuzzy duplicate name pairs in a DataFrame |

---

## 🚀 Usage

```python
import pandas as pd
from eda_toolkit.diagnostics import missing_values
from eda_toolkit.visualization import corr_plot, scatter_plot, outliers_plot
from eda_toolkit.styling import make_pretty, view_df
from eda_toolkit.extractors import extract_nr
from eda_toolkit.name_matching import find_fuzzy_name_duplicates

df = pd.read_csv("data.csv")

# 1. What am I working with?
missing_values(df)                       # missing counts, % and dtypes
make_pretty(df, set_caption="Raw data")  # readable styled preview

# 2. Clean up
df["amount"] = df["description"].apply(extract_nr)   # "R 1 200" -> 1200

# 3. Explore
corr_plot(df)                                    # correlation heatmap
scatter_plot(df, target="price", columns=["area", "rooms"])
outliers_plot(df)                                # box plots, slider per feature

# 4. Inspect specific columns
view_df(df, column="price", focus="max")         # top rows, max highlighted
view_df(df, column="price", focus="heatmap")     # gradient-shaded

# 5. Data quality
find_fuzzy_name_duplicates(df, score_cutoff=90)  # near-duplicate names
```

### `view_df` focus modes

`focus` accepts `"max"`, `"min"`, `"null"`, `"heatmap"`, or `"bar"` — each applies a
different pandas Styler treatment to the sorted result.

---

## 🧩 Dependencies

Installed automatically with `pip install -e .`:

- `pandas`, `numpy`, `plotly`, `IPython`

Optional extras:

| Extra | Package | Needed for |
|---|---|---|
| `[fuzzy]` | `rapidfuzz` | `name_matching.find_fuzzy_name_duplicates` (falls back to `fuzzywuzzy` if absent) |
| `[parquet]` | `pyarrow` | Reading `.parquet` datasets, including the example notebook |
| `[all]` | both | Everything |

---

## ⚠️ Notes

- Plot functions call `fig.show()` directly, so they render inline in a notebook
  rather than returning a figure object.
- `find_fuzzy_name_duplicates` compares every pair of rows — O(n²). Pre-filter large
  datasets before calling it.

---

## 📊 Example data

The notebook in `examples/` uses the **Global AI Tools Landscape (2020–2026)**
dataset by Rhythm Ghai, published on
[Kaggle](https://www.kaggle.com/datasets/rhythmghai/global-ai-tools-landscape-2020-2026)
under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) licence.

Note that this dataset is **synthetically generated** and does not reflect
real-world figures — it is used here only to demonstrate the library. Full
provenance is in [`examples/data/README.md`](examples/data/README.md).

---

## 📝 License

MIT © 2025 Warrick Sabatta

Library code only. Datasets under `examples/data/` are covered by their own
licences — see the table linked above.
