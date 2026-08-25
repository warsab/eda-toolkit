# Example data

Datasets used by the notebooks in `examples/`.

Keep files here small (a few MB at most) — this repo is public and git retains every
version of a binary forever. If a source dataset is large, commit a sampled subset
rather than the full file.

---

## `global_ai_tools_dataset_final.csv`

**Global AI Tools Landscape (2020–2026)** — metadata for 3,000+ AI tools across ten
categories, covering pricing model, open-source status, GitHub stars, company, and
estimated monthly users.

| | |
|---|---|
| **Source** | [kaggle.com/datasets/rhythmghai/global-ai-tools-landscape-2020-2026](https://www.kaggle.com/datasets/rhythmghai/global-ai-tools-landscape-2020-2026) |
| **Author** | Rhythm Ghai (`Rhythm_Ghai`) |
| **Licence** | [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| **Retrieved** | 2026-08-25 |
| **Size** | 3,010 rows × 9 columns (263 KB) |
| **Modified** | No — committed as downloaded |

### ⚠️ This data is synthetic

Per the dataset author, this is a **synthetically generated dataset that does not
reflect real-world data**. Real, well-known AI tools were used as reference points to
model realistic distributions, and the remainder of the rows are generated. It was
built for machine learning experiments, trend analysis, and EDA practice.

**Do not cite any figure in this file as a real-world statistic.** The GitHub star
counts, user numbers, and company attributions for generated entries are fabricated
by design. It is used here purely to demonstrate library functionality.

The author lists Futurepedia, There's An AI For That, GitHub Trending, Hugging Face,
and Product Hunt as reference sources for modelling those distributions.

### Columns

| Column | Type | Description |
|---|---|---|
| `tool_name` | text | Name of the AI tool |
| `category` | text | One of 10 categories (LLM, Image Generation, Coding Assistant, …) |
| `release_year` | int | Release year, 2020–2026 |
| `pricing` | text | Free, Freemium, Paid, or Enterprise |
| `open_source` | text | Yes / No |
| `github_stars` | int | Popularity indicator |
| `company` | text | Organisation behind the tool (14 distinct) |
| `monthly_users` | int | Estimated monthly users |
| `tags` | text | Comma-separated keywords |
