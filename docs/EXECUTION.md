# Execution and verification

Run date: 21 October 2026. Input: documented reference CSV (see DATA_SOURCE.md).

- All 72 code cells executed sequentially in a fresh Python process without errors.
- All 30 analytical questions retained.
- All preparation assertions passed: 891 passenger records, unique complete passenger IDs, 342 survivors, unchanged source columns except explicit missing-port treatment, preserved missing ages and cabins, correct family-size formula, and populated ticket lookup.
- 16 PNG figures and 21 CSV tables generated.
- README image target verified. Representative class-survival chart visually inspected.
- Notebook outputs are actual Python execution results, not retained historical results.

The lightweight runner captures standard output, final expressions and Matplotlib figures; interactive Jupyter frontend rendering was not tested in this environment. Exact tested package versions are pinned in requirements.txt. The user’s original CSV remains unavailable; no byte-equivalence claim is made.
