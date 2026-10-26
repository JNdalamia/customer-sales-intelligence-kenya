# Customer and Sales Intelligence for a Kenyan Retailer

**Capstone type:** Individual Data Science and Analytics project  
**Current stage:** Milestone 1 — problem framing and data acquisition  
**Document version:** 0.1  
**Prepared:** 22 October 2026  
**Primary currency:** Kenyan shilling (KES)

## What is this project about?

I am using a made-up Kenyan retail business to practise using data to answer business questions. I want to understand sales over time, compare stores and products, look at repeat customers, review promotions, and estimate demand for the next month.

The shop, stores, customers, products, prices, costs and transactions are fictional. They were created for this project. They are not records from a real retailer, and the results should not be used to describe the real Kenyan retail market.

## Questions I want to answer

1. How do sales, transaction numbers and units sold change over time?
2. Which stores and counties have the highest sales and estimated gross profit?
3. Which products and categories sell well, and which sell less well?
4. Which customers buy repeatedly, and which repeat customers may be buying less often?
5. Do items covered by a promotion have different sales or estimated profit from other items?
6. How do M-Pesa, cash, card and bank transfer use differ by store and basket size?
7. How many units might each store and product category need next month, and could dates or holidays be relevant?

The plan and the measures for checking the answers are in [`docs/problem_statement.md`](docs/problem_statement.md).

## What data is included?

- 80,000 fictional transaction records from 1 October 2024 to 30 September 2026.
- 175,098 fictional sales lines (each line is one product on a receipt).
- 4,000 fictional customers, 250 fictional products, eight fictional stores and 24 made-up promotion schedules.
- A small Kenya National Bureau of Statistics (KNBS) CPI extract for August and September 2026.
- A data inventory, data dictionary, validation report and code for generating the fictional business data again.

**CPI limitation:** The public CPI file has only two months. It is included as an example of documented public data, but it is not enough to compare inflation with sales for all 24 months. I need to download and record more official monthly CPI data before doing that analysis.

The Kenya census and public-holiday links are listed as possible future sources. Their full data files are not included yet, so I do not count them as completed data collection.

## How I made the fictional data

I wrote a Python script called `src/generate_synthetic_data.py`. It uses a fixed random seed (`20261026`) so that the data can be made again using the same steps. The script creates the store, product, customer, promotion, transaction and sales-line files.



## Tools planned

I plan to use Python and pandas for data preparation and analysis, PostgreSQL for SQL practice, Power BI for a dashboard, Jupyter notebooks for exploration, and Git/GitHub to keep track of the project.

## Current status

This milestone includes the problem statement, seven business questions, success measures, generated raw data, a small public CPI extract, a source inventory and basic data checks. A full 24-month CPI series and verified holiday-date file are still future tasks.