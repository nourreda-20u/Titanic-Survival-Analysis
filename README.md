<p align="center">
  <img src="assets/titanic-cover.jpg" alt="Titanic (1997)" width="100%">
</p>

# Titanic Survival Analysis

Exploratory analysis of **891 passengers** using Python, Pandas, NumPy, Matplotlib and Seaborn. The project examines how survival varies by sex, class, age, fare and travel groups.

[Notebook](notebooks/titanic_analysis.ipynb) · [Report](docs/PROJECT_REPORT.md) · [Prepared data](data/processed/titanic_prepared.csv)

## Key findings

| Comparison | Survival rate |
|---|---|
| Overall | **38.38%** — 342 of 891 passengers |
| Female / Male | **74.20% / 18.89%** |
| First / Second / Third class | **62.96% / 47.28% / 24.24%** |
| Children under 16 / Adults | **59.04% / 38.19%** — recorded ages only |

![Survival by sex and passenger class](outputs/figures/survival_by_sex_and_class.png)

## What the project includes

- Data-quality checks and documented preparation decisions.
- 30 analytical questions, 16 charts and 21 exported tables.
- Missing ages and cabins preserved; plausible outliers retained.
- A reproducible notebook and execution script.

## Run locally

With Python 3.11+ installed, run from the project folder:

```bash
python -m pip install -r requirements.txt
python scripts/run_analysis.py
```

[Full setup guide](docs/PROJECT_GUIDE.md)

## Data source

[Kaggle Titanic](https://www.kaggle.com/competitions/titanic/data), using the [Data Science Dojo reference CSV](https://github.com/datasciencedojo/datasets/blob/master/titanic.csv). The original workshop CSV was not supplied; [provenance details](docs/DATA_SOURCE.md) document the reference used.

Results describe associations in this sample. Age comparisons exclude 177 missing ages; class, fare and other characteristics overlap.

---

**Nour Reda** · [LinkedIn](https://www.linkedin.com/in/nour-reda-349b43321/)

<sub>Cover: user-supplied Titanic (1997) image. [Asset notes](assets/ATTRIBUTION.md).</sub>
