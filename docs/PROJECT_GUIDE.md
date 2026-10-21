# Project guide

## Run

Extract the ZIP, open a terminal in Titanic_Survival_Analysis and follow README setup. Use `python scripts/run_analysis.py` to rebuild the notebook outputs, prepared CSV, figures and tables. Input is local; execution requires no download or account.

## Substitute your original CSV

Back up the reference input, replace `data/raw/titanic_dataset.csv` with your original file and rerun. Update DATA_SOURCE, source hash, README results and narrative interpretations if the outputs differ. The 891-row assertion deliberately restricts this workshop to its documented sample; using a different population requires reviewing the assumptions, quartile labels and narrative, not merely removing the assertion.

## Read and customize

Start with README, then the notebook, then PROJECT_REPORT. Each chart remains in a separate simple cell. Keep source data unchanged and record future cleaning decisions. The executable notebook is the analysis source; the runner uses the same cells rather than duplicating calculations.

## Upload to GitHub

Create a repository such as `titanic-survival-analysis`. Upload the contents of this project folder, including README, notebooks, docs, scripts, data and outputs. Do not upload virtual environments or caches. The archive contains only the supplied original notebook and can be omitted from a public showcase if you prefer a smaller repository. Source attribution must remain. GitHub can render the executed notebook and README images directly.

Suggested description: Exploratory analysis of Titanic passenger survival using Python, Pandas and Seaborn, with transparent data-quality decisions, 30 analytical questions and reproducible outputs.

No credentials, remote push or deployment are needed to review the package. Repository: https://github.com/nourreda-20u/Titanic-Survival-Analysis
