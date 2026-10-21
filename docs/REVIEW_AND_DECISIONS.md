# Review and analytical decisions

The input already contained a detailed project brief, data dictionary, quality review, engineered features, 30 analyses, limitations and conclusions. Its valid analysis and section order were preserved.

| Finding | Change / decision |
|---|---|
| CSV absent from attachment | Explicitly document and use a public reference copy for execution |
| Flat local loading/export paths | Resolve project root and use raw/processed/output directories |
| Final export was present and valid | Retain its purpose; place output under data/processed |
| A full prepared dataframe was displayed | Replace with head() for readable GitHub rendering |
| Final `%whos` was development-only | Remove from deliverable |
| Charts and tables existed mainly inside notebook | Export PNGs and CSV evidence tables |
| Preparation checks mostly printed values | Add assertions for key, row, outcome, source measurement and feature consistency |
| Notebook retained historic outputs | Recompute outputs sequentially from the documented input |
| Referenced another notebook in an explanation | Make explanation self-contained |

No age imputation, row deletion, fare capping or automatic outlier removal was introduced. Missing port labels are reporting categories, not recovered facts. Source fields other than Embarked must remain exactly equal after feature creation. Grouped tables include denominators and survivor counts. No causal or ML accuracy claims were added.

Execution evidence and exact dependency versions are in `EXECUTION.md` and `requirements.txt`. Reference-data results should be rerun if the original CSV is substituted.
