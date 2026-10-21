# Titanic analysis — project report

## Objective and questions

Understand which recorded passenger characteristics are associated with survival. Main questions cover overall survival; sex and class contrasts; age and child comparisons; family and ticket groups; fare quartiles; embarkation; cabin availability; and confounding. All 30 workshop questions remain in the notebook.

## Data and grain

One row represents one passenger, not one ticket or family. There are 891 passengers, 681 distinct tickets and 342 survivors. The 12 source fields include the binary outcome, identifiers, demographic variables and travel information. This is a training sample, not a census of the ship.

## Quality assessment and preparation

Check source dimensions, key completeness and uniqueness, exact duplicates, coded categories, nonnegative fares and counts, age bounds and integer family counts. Review IQR flags for four variables without automatically deleting records.

Age is missing for 177 passengers (19.87%), cabin text for 687 (77.10%), embarkation for two (0.22%). Retain missing age and cabin text, explicitly label missing port Unknown, and retain every passenger. Known-age comparisons use 714 records. Prepared data is for descriptive reporting, not a fully imputed ML design matrix.

Features include readable class/outcome labels, FamilySize, Travel_Group, AgeGroup, Age_Category, FareGroup, Cabin_Info, TicketGroupSize, Ticket_Type and Title. A validated many-to-one ticket merge preserves passenger grain. Age intervals are left-closed: [0,16), [16,30), [30,45), [45,60), [60,infinity). Fare quartiles are sample-relative; ties make group counts unequal.

## Findings

| Comparison | Evidence | Interpretation |
|---|---|---|
| Overall | 342/891 survived (38.38%) | Most sampled passengers did not survive |
| Sex | Female 74.20%, male 18.89% | Large recorded-group contrast |
| Class | First 62.96%, second 47.28%, third 24.24% | Strong class gradient |
| Sex within class | First-class females 91/94 (96.81%); third-class males 47/347 (13.54%) | Combining dimensions gives more context |
| Known age | Under 16: 49/83 (59.04%); adults: 241/631 (38.19%) | Excludes 177 unknown ages |
| Family | Recorded family 50.56%, alone 30.35% | Alone means no recorded relatives, not necessarily no companions |
| Fare | Highest quartile 58.11%, lowest 19.73% | Fare overlaps with passenger class |
| Cabin documentation | Available 136/204 (66.67%), missing 206/687 (29.99%) | Missing cabin does not mean no cabin |
| Ticket groups | Shared 179/344 (52.03%), unique 163/547 (29.80%) | Ticket sharing is measured only in this sample |

Sex, class and cabin availability show clear descriptive contrasts, but this is not a formal ranking of independent causal drivers. Cherbourg has a higher first-class share than Southampton, illustrating why aggregate port survival can reflect passenger composition. Class-by-fare and sex-by-class tables provide stratified context.

## Limitations

Missingness may be systematic. Small subgroups and single-person titles produce unstable percentages. Family and ticket groups may have related outcomes. Correlations use pairwise available observations; age correlations use fewer records. Class is coded numerically but ordinal. Fare may reflect shared-ticket context and should not be treated as normalized individual expenditure. Multiple exploratory comparisons are not formal significance tests. Rescue access and exact locations are unavailable. The raw source used for execution is a documented reference copy rather than the unavailable workshop CSV.

## Conclusion

Large survival differences appear across recorded sex and passenger class. Children with known ages and passengers with recorded family also have higher observed survival. Fare, port and cabin-documentation patterns overlap with class, so simple comparisons require context. The project demonstrates transparent preparation, passenger-grain validation, grouped analysis and cautious evidence-based reporting.

## Delivery status

Completed: reviewed and executed notebook; original backup; raw reference and prepared CSV; exported charts and tables; reproducible script; documentation and project guide. The project is prepared for publication to the Titanic-Survival-Analysis repository. Machine learning and a separate BI dashboard are outside this analysis scope.
