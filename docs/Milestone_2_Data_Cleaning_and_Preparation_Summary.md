# Milestone 2: Data Cleaning and Preparation

## Project summary

In this milestone, I used Python and pandas to inspect, clean, validate, and prepare the synthetic retail sales-line dataset for further analysis. I developed reusable functions to standardise text and column names, convert data types, check duplicates, review missing values, and flag unusual values. The aim was to improve data consistency while retaining potentially meaningful sales records.

### 1. Data inspection and cleaning

I loaded the raw sales-line dataset and examined its structure, data types, descriptive statistics, missing values, and exact duplicate records. The dataset initially contained **175,098 rows and 17 columns**, covering transactions from 1 October 2024 to 30 September 2026.

The cleaning pipeline standardised column names and removed leading and trailing spaces from text fields. I converted the transaction date to a datetime format and the relevant sales and quantity fields to numeric types. Invalid conversions were configured to become missing values for review. The pipeline also checked for fully identical duplicate rows and standardised blank identifier fields without automatically changing identifier values.

### 2. Data quality results

The notebook recorded the following findings:

| Data quality check | Result |
|---|---:|
| Raw records | 175,098 |
| Records after basic cleaning | 175,098 |
| Original columns | 17 |
| Columns after feature engineering | 22 |
| Exact duplicate rows removed | 0 |
| Duplicate transaction-line keys | 0 |
| Missing transaction IDs | 0 |
| Discounts outside the 0–100 range | 0 |
| Missing promotion IDs | 175,062 (99.98%) |
| Negative quantity rows | 4,430 |
| Net-sales outliers flagged using IQR | 14,212 |

The record count remained unchanged because no fully identical duplicate rows were found. Missing promotion IDs were retained in the dataset rather than automatically filled. The notebook also identified 4,430 negative-quantity rows for review; the data contains 4,430 records with a `RETURN` transaction status. This is consistent with the negative quantities potentially representing returns, although the notebook does not explicitly verify a one-to-one match.

### 3. Outlier investigation

I applied the interquartile range (IQR) method to `net_sales_kes` to identify unusually high or low sales-line values. The method flagged **14,212 rows** for further investigation. These records were retained because an unusually large or small value is not necessarily an error.

I also checked negative quantities, discount values, negative prices and costs, and transaction statuses outside the expected categories of `SALE`, `RETURN`, and `VOID`. The notebook recorded no invalid discounts, negative values in the checked price and cost fields, or unknown transaction statuses.

### 4. Feature engineering

After cleaning, I created five additional features to support subsequent analysis:

- `year` — the transaction year.
- `month` — the transaction month as a number.
- `year_month` — the year and month combined for monthly analysis.
- `day_name` — the weekday on which the transaction occurred.
- `discount_group` — a category based on the discount percentage.

These additions increased the dataset from 17 to **22 columns**, while retaining all 175,098 rows. In the uploaded notebook, `discount_group` is the promotion-related analytical feature shown; a separate `promotion_category` column is not created.

### 5. Saving the prepared dataset

I completed final checks on the dataset's dimensions, date range, transaction-line key uniqueness, discount validity, and transaction ID completeness. I then saved the prepared dataset separately from the raw file as:

`data/processed/sales_lines_clean.csv`

This allows the original data to remain unchanged and the prepared dataset to be reused in later stages of the project.

## Conclusion

Milestone 2 established a repeatable pandas workflow for inspecting and preparing the synthetic retail sales data. The notebook documents the key data-quality findings, retains potentially meaningful returns and outliers, and creates date and discount features for future analysis. The final dataset contains **175,098 records and 22 columns** and is saved for the next stage of the project.
