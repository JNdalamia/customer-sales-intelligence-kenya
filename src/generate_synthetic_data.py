"""Make fictional retail data for my capstone project.

The stores, customers, products, prices and transactions in this project are made up.
This script uses normal Python lists, dictionaries, loops and CSV files.
"""

from pathlib import Path
from datetime import date, timedelta
import csv
import json
import random
import sys


# Find the main project folder based on where this script is saved.
PROJECT_FOLDER = Path(__file__).resolve().parents[1]
DATA_FOLDER = PROJECT_FOLDER / "data" / "raw" / "synthetic"
SAMPLE_FOLDER = PROJECT_FOLDER / "data" / "sample"
DATA_FOLDER.mkdir(parents=True, exist_ok=True)
SAMPLE_FOLDER.mkdir(parents=True, exist_ok=True)

# Keeping the seed the same makes the random data repeatable.
SEED = 20261026
random.seed(SEED)

# The fictional sales cover two years.
START_DATE = date(2024, 10, 1)
END_DATE = date(2026, 9, 30)
NUMBER_OF_DAYS = (END_DATE - START_DATE).days + 1


def save_csv(file_path, columns, rows):
    """Save a list of dictionaries to a CSV file."""
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def random_date():
    """Choose a random date inside the two-year period."""
    days_after_start = random.randint(0, NUMBER_OF_DAYS - 1)
    return START_DATE + timedelta(days=days_after_start)


# PART 1: Make eight fictional stores.
store_details = [
    ("ST001", "Nairobi CBD", "Nairobi"),
    ("ST002", "Westlands", "Nairobi"),
    ("ST003", "Thika", "Kiambu"),
    ("ST004", "Nakuru Town", "Nakuru"),
    ("ST005", "Mombasa Central", "Mombasa"),
    ("ST006", "Nyali", "Mombasa"),
    ("ST007", "Kisumu Central", "Kisumu"),
    ("ST008", "Eldoret", "Uasin Gishu"),
]
stores = []
for store_id, store_name, county in store_details:
    stores.append({
        "store_id": store_id,
        "store_name": store_name,
        "county": county,
        "region": "Kenya",
        "store_type": "Urban",
        "is_fictional": True,
    })
save_csv(DATA_FOLDER / "stores_synthetic.csv", list(stores[0].keys()), stores)


# PART 2: Make 250 products with made-up prices and costs.
categories = [
    "Food & Grocery", "Home & Kitchen", "Personal Care", "Electronics",
    "Clothing", "Stationery", "Baby Products", "Sports & Outdoors",
]
brands = ["Jirani", "Tawi", "Bahari", "Mwangaza", "Kipepeo", "Milele", "Imara", "Pamoja"]
products = []
for number in range(1, 251):
    category = categories[(number - 1) % len(categories)]
    price = round(random.uniform(80, 6500), 2)
    cost = round(price * random.uniform(0.48, 0.78), 2)
    products.append({
        "product_id": f"SKU{number:04d}",
        "product_name": f"{category.split()[0]} Item {number:03d}",
        "category": category,
        "brand": brands[(number - 1) % len(brands)],
        "unit_cost_kes": cost,
        "list_price_kes": price,
        "is_fictional": True,
    })
save_csv(DATA_FOLDER / "products_synthetic.csv", list(products[0].keys()), products)


# PART 3: Make 4,000 fictional customers.
counties = ["Nairobi", "Kiambu", "Nakuru", "Mombasa", "Kisumu", "Uasin Gishu"]
customers = []
for number in range(1, 4001):
    registration_date = random_date()
    existing_customer = random.random() < 0.18

    if existing_customer:
        first_purchase_date = START_DATE - timedelta(days=random.randint(1, 729))
        customer_status = "pre_existing"
    else:
        first_purchase_date = registration_date
        customer_status = "observed_new"

    customers.append({
        "customer_id": f"C{number:05d}",
        "registration_date": registration_date.isoformat(),
        "first_purchase_date": first_purchase_date.isoformat(),
        "customer_status_at_window_start": customer_status,
        "county": random.choice(counties),
        "loyalty_tier": random.choices(["Standard", "Silver", "Gold"], weights=[72, 20, 8])[0],
        "is_fictional": True,
    })
save_csv(DATA_FOLDER / "customers_synthetic.csv", list(customers[0].keys()), customers)


# PART 4: Make 24 fictional promotion schedules.
promotions = []
for number in range(1, 25):
    promotion_start = START_DATE + timedelta(days=random.randint(0, NUMBER_OF_DAYS - 28))
    promotion_end = min(END_DATE, promotion_start + timedelta(days=random.randint(7, 21)))
    promotions.append({
        "promotion_id": f"PR{number:03d}",
        "promotion_name": f"Campaign {number:02d}",
        "store_id": random.choice(stores)["store_id"],
        "product_id": random.choice(products)["product_id"],
        "start_date": promotion_start.isoformat(),
        "end_date": promotion_end.isoformat(),
        "discount_pct": random.choice([5, 10, 15, 20, 25]),
        "is_synthetic": True,
    })
save_csv(DATA_FOLDER / "promotions_synthetic.csv", list(promotions[0].keys()), promotions)


# Prepare the columns for the two main files.
transaction_columns = [
    "transaction_id", "transaction_date", "store_id", "customer_id",
    "payment_method", "transaction_status", "line_count", "is_synthetic",
]
sales_line_columns = [
    "transaction_id", "line_number", "transaction_date", "store_id", "customer_id",
    "product_id", "quantity", "list_unit_price_kes", "discount_pct",
    "net_unit_price_kes", "gross_sales_kes", "net_sales_kes", "unit_cost_kes",
    "gross_profit_kes", "promotion_id", "transaction_status", "is_synthetic",
]

# Keep these totals so I can report how much data was made.
transaction_count = 80000
sales_line_count = 0
status_counts = {"SALE": 0, "RETURN": 0, "VOID": 0}
transaction_sample = []
sales_line_sample = []

# PART 5: Make the transactions and the products on each receipt.
# Write rows as we go so the script does not have to keep all sales lines in memory.
transaction_file = DATA_FOLDER / "transactions_synthetic.csv"
sales_line_file = DATA_FOLDER / "sales_lines_synthetic.csv"

with open(transaction_file, "w", newline="", encoding="utf-8") as tx_file, \
     open(sales_line_file, "w", newline="", encoding="utf-8") as line_file:

    transaction_writer = csv.DictWriter(tx_file, fieldnames=transaction_columns)
    line_writer = csv.DictWriter(line_file, fieldnames=sales_line_columns)
    transaction_writer.writeheader()
    line_writer.writeheader()

    for number in range(1, transaction_count + 1):
        transaction_id = f"TX{number:07d}"
        transaction_date = random_date()
        store_id = random.choice(stores)["store_id"]
        customer_id = random.choice(customers)["customer_id"]
        status = random.choices(["SALE", "RETURN", "VOID"], weights=[965, 25, 10])[0]
        payment_method = random.choices(
            ["M-Pesa", "Cash", "Card", "Bank Transfer"], weights=[56, 25, 14, 5]
        )[0]
        number_of_lines = random.choices([1, 2, 3, 4, 5], weights=[34, 32, 19, 10, 5])[0]

        # Choose different products for the receipt. One receipt can have many lines.
        chosen_products = random.sample(products, number_of_lines)

        for line_number, product in enumerate(chosen_products, start=1):
            quantity = random.choices([1, 2, 3, 4], weights=[70, 20, 8, 2])[0]
            promotion_id = ""
            discount = random.choice([0, 0, 0, 5, 10])

            # Check whether this store, product and date are covered by a promotion.
            for promotion in promotions:
                if (promotion["store_id"] == store_id
                        and promotion["product_id"] == product["product_id"]
                        and promotion["start_date"] <= transaction_date.isoformat() <= promotion["end_date"]):
                    promotion_id = promotion["promotion_id"]
                    discount = promotion["discount_pct"]
                    break

            list_price = product["list_price_kes"]
            unit_cost = product["unit_cost_kes"]
            net_unit_price = round(list_price * (1 - discount / 100), 2)
            gross_sales = round(list_price * quantity, 2)
            net_sales = round(net_unit_price * quantity, 2)
            gross_profit = round(net_sales - unit_cost * quantity, 2)

            # Returns have negative quantities and values. Voids have zero sales value.
            if status == "RETURN":
                quantity = -quantity
                gross_sales = -gross_sales
                net_sales = -net_sales
                gross_profit = -gross_profit
            elif status == "VOID":
                gross_sales = 0
                net_sales = 0
                gross_profit = 0

            sales_line = {
                "transaction_id": transaction_id,
                "line_number": line_number,
                "transaction_date": transaction_date.isoformat(),
                "store_id": store_id,
                "customer_id": customer_id,
                "product_id": product["product_id"],
                "quantity": quantity,
                "list_unit_price_kes": list_price,
                "discount_pct": discount,
                "net_unit_price_kes": net_unit_price,
                "gross_sales_kes": gross_sales,
                "net_sales_kes": net_sales,
                "unit_cost_kes": unit_cost,
                "gross_profit_kes": gross_profit,
                "promotion_id": promotion_id,
                "transaction_status": status,
                "is_synthetic": True,
            }
            line_writer.writerow(sales_line)
            sales_line_count += 1
            if len(sales_line_sample) < 2500:
                sales_line_sample.append(sales_line)

        transaction = {
            "transaction_id": transaction_id,
            "transaction_date": transaction_date.isoformat(),
            "store_id": store_id,
            "customer_id": customer_id,
            "payment_method": payment_method,
            "transaction_status": status,
            "line_count": number_of_lines,
            "is_synthetic": True,
        }
        transaction_writer.writerow(transaction)
        status_counts[status] += 1
        if len(transaction_sample) < 1000:
            transaction_sample.append(transaction)


# PART 6: Save small samples so I can inspect the data more quickly.
save_csv(SAMPLE_FOLDER / "transactions_synthetic_sample.csv", transaction_columns, transaction_sample)
save_csv(SAMPLE_FOLDER / "sales_lines_synthetic_sample.csv", sales_line_columns, sales_line_sample)
save_csv(SAMPLE_FOLDER / "customers_synthetic_sample.csv", list(customers[0].keys()), customers[:100])


# PART 7: Save a small record of the files and settings used.
metadata = {
    "random_seed": SEED,
    "python_version": sys.version.split()[0],
    "data_start": START_DATE.isoformat(),
    "data_end": END_DATE.isoformat(),
    "transactions": transaction_count,
    "sales_lines": sales_line_count,
    "customers": len(customers),
    "products": len(products),
    "stores": len(stores),
    "promotions": len(promotions),
    "transaction_status_counts": status_counts,
    "all_business_data_is_fictional": True,
}
with open(DATA_FOLDER / "generation_metadata.json", "w", encoding="utf-8") as file:
    json.dump(metadata, file, indent=2)

print("Finished creating the fictional retail data.")
print(f"Transactions: {transaction_count:,}")
print(f"Sales lines: {sales_line_count:,}")
print(f"Customers: {len(customers):,}")
print("Transaction status counts:", status_counts)
print("All business data created by this script is fictional.")
