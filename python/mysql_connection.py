import mysql.connector
import pandas as pd

# -----------------------------------
# 1. Connect to MySQL
# -----------------------------------

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9977182978",
    database="retail_intelligence"
)

print("MySQL connection successful!")


# -----------------------------------
# 2. Load data from MySQL
# -----------------------------------

query = """
SELECT
    o.order_id,
    o.order_date,
    c.customer_id,
    c.customer_name,
    c.segment,
    c.city,
    c.state,
    r.region_name,
    p.product_id,
    p.product_name,
    p.category,
    p.sub_category,
    p.cost_price,
    o.quantity,
    o.selling_price,
    o.discount
FROM orders o

JOIN customers c
    ON o.customer_id = c.customer_id

JOIN products p
    ON o.product_id = p.product_id

JOIN regions r
    ON c.region_id = r.region_id
"""

df = pd.read_sql(query, connection)

connection.close()

print("Data loaded successfully!")
print("Total rows:", len(df))


# -----------------------------------
# 3. Calculate Revenue
# -----------------------------------

df["revenue"] = (
    df["quantity"]
    * df["selling_price"]
    * (1 - df["discount"])
)


# -----------------------------------
# 4. Calculate Cost
# -----------------------------------

df["cost"] = (
    df["quantity"]
    * df["cost_price"]
)


# -----------------------------------
# 5. Calculate Profit
# -----------------------------------

df["profit"] = (
    df["revenue"]
    - df["cost"]
)


# -----------------------------------
# 6. Calculate Profit Margin
# -----------------------------------

df["profit_margin"] = (
    df["profit"]
    / df["revenue"]
    * 100
)


# -----------------------------------
# 7. Display Executive KPIs
# -----------------------------------

total_orders = df["order_id"].nunique()
total_customers = df["customer_id"].nunique()
total_products = df["product_id"].nunique()

total_revenue = df["revenue"].sum()
total_cost = df["cost"].sum()
total_profit = df["profit"].sum()

overall_margin = (
    total_profit / total_revenue * 100
)


print("\n========== EXECUTIVE KPIs ==========")

print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Total Products:", total_products)

print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Cost: ₹{total_cost:,.2f}")
print(f"Total Profit: ₹{total_profit:,.2f}")
print(f"Profit Margin: {overall_margin:.2f}%")


# -----------------------------------
# 8. Show sample analysis
# -----------------------------------

print("\n========== SAMPLE DATA ==========")

print(
    df[
        [
            "order_id",
            "customer_name",
            "product_name",
            "quantity",
            "discount",
            "revenue",
            "cost",
            "profit",
            "profit_margin"
        ]
    ].head(10)
)


# -----------------------------------
# 9. Save processed data
# -----------------------------------

df.to_csv(
    "data/processed/sales_analysis.csv",
    index=False
)

print("\nProcessed data saved successfully!")
print("File: data/processed/sales_analysis.csv")