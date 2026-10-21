# 2) Data Understanding

### Column Dictionary

| Column | Meaning | Analytical role |
|---|---|---|
| PassengerId | Passenger identifier | Identifier |
| Survived | 0 = did not survive; 1 = survived | Binary outcome |
| Pclass | 1 = first; 2 = second; 3 = third class | Ordered category |
| Name | Passenger full name | Text; can provide a title |
| Sex | Recorded male/female category | Category |
| Age | Age in years | Numerical; fractional ages represent infants |
| SibSp | Siblings or spouses aboard | Numerical count |
| Parch | Parents or children aboard | Numerical count |
| Ticket | Ticket identifier | Identifier; useful for shared-ticket analysis |
| Fare | Recorded ticket fare | Numerical |
| Cabin | Recorded cabin number(s) | Text with substantial missingness |
| Embarked | C = Cherbourg; Q = Queenstown; S = Southampton | Category |

Each row represents **one passenger**, not one ticket or one family. Several passengers may share a ticket.

## Engineered columns

| Field | Definition |
|---|---|
| Survival_Status | Readable mapping of Survived |
| Class_Name | First, Second, Third mapping |
| FamilySize | SibSp + Parch + 1 |
| Travel_Group | Alone when FamilySize=1; otherwise With recorded family |
| AgeGroup | Left-closed age intervals; missing age remains missing |
| Age_Category | Child (<16), Adult (16+), Unknown |
| FareGroup | Four sample-relative qcut quartiles |
| Cabin_Info | Available or Missing cabin text |
| TicketGroupSize | Passenger records with same Ticket in this sample |
| Ticket_Type | Shared ticket when TicketGroupSize>1; otherwise Unique ticket |
| Title | Name text after comma and before period |

Original numeric fields remain numeric. Zero and missing are not interchangeable. Prepared CSV exports categories as text and missing values as empty fields; use Pandas default CSV NA parsing when reloading.
