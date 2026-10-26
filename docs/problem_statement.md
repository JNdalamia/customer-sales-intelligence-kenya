# Problem Framing and Business Questions

## Project purpose

I am using a fictional Kenyan retail chain to practise how data can help managers understand sales, customers, stores and products. I also want to check whether promotions are linked with different sales results and make a simple forecast of next month's demand.

All the shop, customer, product, price, cost and transaction data are made up for this project. They are not facts about a real business.

## Problem statement

The fictional retailer needs a clearer picture of what is selling, where sales are happening and whether customers keep coming back. Managers could use this information to decide which products to review for stock, which stores need attention and which customers might need a reminder or offer. These questions are difficult because the information needs to be compared fairly, customer history starts at a fixed date, and a link between a promotion and higher sales does not prove that the promotion caused the change. I will use two years of fictional sales data and a small amount of Kenyan public data to explore these questions and estimate next month's demand. I will check my calculations, compare my forecast with simple methods and explain where the data is limited.

## Who could use the results?

| Person | How the results could help |
|---|---|
| Merchandising manager | See which products and categories sell more or less. |
| Regional operations manager | Compare store results and decide which stores need a closer look. |
| Marketing lead | Understand repeat buying and review promotion results. |
| Finance manager | Compare sales and estimated product profit by store and category. |
| Stock planner | Use the demand forecast as a starting point for stock planning. |

## Business questions, data and success checks

| No. | Question | Data I will use | How I will check my work |
|---|---|---|---|
| 1 | How do sales, transaction numbers and units sold change over time? | Transactions and sales lines, grouped by date or month. | Produce clear daily or monthly totals and check that the totals agree when the same rules are used. |
| 2 | Which stores and counties have the highest sales and estimated gross profit? | Sales lines joined to the store list. | Rank stores and counties, and label profit as estimated because product costs are made up. |
| 3 | Which products and categories sell well, and which sell less well? | Sales lines joined to the product list. | Compare units, sales and estimated profit using the same filters. |
| 4 | Which customers buy repeatedly, and which repeat customers may be buying less often? | Customer and transaction tables. | Write down the rules for each customer group and do not label every one-time customer as lost. |
| 5 | Do items in a promotion have different sales or estimated profit? | Sales lines and the made-up promotion dates. | Compare similar products and stores where possible. Explain that the result shows a relationship, not proof that a promotion caused it. |
| 6 | How do payment methods differ by store and basket size? | The transaction table and sales totals calculated for each receipt. | Count each transaction once and check that payment totals agree with the transaction records. |
| 7 | How many units might each store and category need next month? Could dates or holidays matter? | Monthly product sales; later, more KNBS CPI data and a checked holiday calendar. | Compare the forecast with a simple previous-month estimate and report how far the forecast was from actual values. |

## How I will measure success

1. The project has seven clear questions and explains why each matters.
2. I have saved the generated business data and the public source extract in the project folders.
3. I have written down what each file and important column means.
4. The data can be generated again using the included script and fixed seed.
5. The basic checks pass, including unique transaction IDs and valid links between transactions, customers, products and stores.
6. My sales calculations use consistent rules for sales, returns and void transactions.
7. I compare the forecast with a simple baseline instead of claiming it is accurate without checking.
8. I clearly identify the business data as fictional and explain the limits of the public data.

## Data included and its limits

The fictional data covers 1 October 2024 to 30 September 2026. It includes eight stores in six counties, 250 products, 4,000 customers, 80,000 transactions and the product lines for those transactions. Prices, costs, payment choices and promotion schedules are generated for practice.

The KNBS CPI file currently includes only August and September 2026. I will need a longer, verified series before comparing CPI with sales over the full two years. Census population tables and a date-level public-holiday file are possible additions, but they have not been collected in this milestone.

## Simple rules I will follow

- I will count transactions from the transaction table, not by counting product lines.
- I will total line items before calculating the average basket value for each receipt.
- I will keep returns and voids separate and explain how they are handled.
- Product costs and gross profit are fictional estimates. They are not the shop's real costs or profit.
- I will not say a promotion or a holiday caused a sales change just because they happened at the same time.
- I will not fill missing CPI months with made-up public figures.

## Sources identified

- [KNBS September 2026 CPI release](https://repository.knbs.or.ke/entities/publication/a35679f7-4a46-4f87-997e-f431def2e297) — the current public extract is limited to two months; the item states CC BY-NC 4.0 terms.
- [KNBS 2019 census results](https://www.knbs.or.ke/2019-kenya-population-and-housing-census-results/) and [population tables](https://www.knbs.or.ke/reports/kenya-census-2019/) — identified as possible future sources; not included as raw data here.
- [Kenya Law Public Holidays Act](https://new.kenyalaw.org/akn/ke/act/1912/21/eng%402024-04-26/source) and [Ministry of Interior page](https://www.interior.go.ke/ova_doc/public-holidays-act-cap-110/) — legal background, but not a complete calendar of holiday dates.
- [Ministry of Education news and circulars](https://www.education.go.ke/news) — optional future source; not used in this milestone.
