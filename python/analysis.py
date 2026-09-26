import pandas as pd

# ============================================================
# RETAIL SALES & PROFIT INTELLIGENCE PROJECT
# Python Business Analysis
# ============================================================

# ------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------

df = pd.read_csv("data/processed/sales_analysis.csv")

print("Data loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# ------------------------------------------------------------
# 2. CALCULATE BUSINESS METRICS
# ------------------------------------------------------------

df["revenue"] = (
    df["quantity"]
    * df["selling_price"]
    * (1 - df["discount"])
)

df["cost"] = (
    df["quantity"]
    * df["cost_price"]
)

df["profit"] = (
    df["revenue"]
    - df["cost"]
)

df["profit_margin"] = (
    df["profit"]
    / df["revenue"]
    * 100
)


# ============================================================
# 3. EXECUTIVE KPIs
# ============================================================

total_orders = df["order_id"].nunique()
total_customers = df["customer_id"].nunique()
total_products = df["product_id"].nunique()

total_revenue = df["revenue"].sum()
total_cost = df["cost"].sum()
total_profit = df["profit"].sum()

overall_margin = (
    total_profit / total_revenue * 100
)

print("\n" + "=" * 60)
print("EXECUTIVE KPIs")
print("=" * 60)

print(f"Total Orders:      {total_orders:,}")
print(f"Total Customers:   {total_customers:,}")
print(f"Total Products:    {total_products:,}")
print(f"Total Revenue:     ₹{total_revenue:,.2f}")
print(f"Total Cost:        ₹{total_cost:,.2f}")
print(f"Total Profit:      ₹{total_profit:,.2f}")
print(f"Profit Margin:     {overall_margin:.2f}%")


# ============================================================
# 4. TOP 10 PRODUCTS BY REVENUE
# ============================================================

top_products_revenue = (
    df.groupby("product_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n" + "=" * 60)
print("TOP 10 PRODUCTS BY REVENUE")
print("=" * 60)

for product, revenue in top_products_revenue.items():
    print(f"{product:<30} ₹{revenue:,.2f}")


# ============================================================
# 5. TOP 10 PRODUCTS BY PROFIT
# ============================================================

top_products_profit = (
    df.groupby("product_name")["profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n" + "=" * 60)
print("TOP 10 PRODUCTS BY PROFIT")
print("=" * 60)

for product, profit in top_products_profit.items():
    print(f"{product:<30} ₹{profit:,.2f}")


# ============================================================
# 6. TOP 10 PRODUCTS BY PROFIT MARGIN
# ============================================================

product_margin = (
    df.groupby("product_name")
    .agg(
        revenue=("revenue", "sum"),
        profit=("profit", "sum")
    )
)

product_margin["profit_margin"] = (
    product_margin["profit"]
    / product_margin["revenue"]
    * 100
)

top_margin_products = (
    product_margin
    .sort_values("profit_margin", ascending=False)
    .head(10)
)

print("\n" + "=" * 60)
print("TOP 10 PRODUCTS BY PROFIT MARGIN")
print("=" * 60)

for product, row in top_margin_products.iterrows():
    print(
        f"{product:<30} "
        f"{row['profit_margin']:.2f}%"
    )


# ============================================================
# 7. TOP 10 CUSTOMERS BY REVENUE
# ============================================================

top_customers_revenue = (
    df.groupby(["customer_id", "customer_name"])["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n" + "=" * 60)
print("TOP 10 CUSTOMERS BY REVENUE")
print("=" * 60)

for (customer_id, customer_name), revenue in top_customers_revenue.items():
    print(
        f"{customer_name:<25} "
        f"₹{revenue:,.2f}"
    )


# ============================================================
# 8. TOP 10 CUSTOMERS BY PROFIT
# ============================================================

top_customers_profit = (
    df.groupby(["customer_id", "customer_name"])["profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n" + "=" * 60)
print("TOP 10 CUSTOMERS BY PROFIT")
print("=" * 60)

for (customer_id, customer_name), profit in top_customers_profit.items():
    print(
        f"{customer_name:<25} "
        f"₹{profit:,.2f}"
    )


# ============================================================
# 9. CATEGORY PERFORMANCE
# ============================================================

category_analysis = (
    df.groupby("category")
    .agg(
        revenue=("revenue", "sum"),
        cost=("cost", "sum"),
        profit=("profit", "sum"),
        orders=("order_id", "nunique")
    )
)

category_analysis["profit_margin"] = (
    category_analysis["profit"]
    / category_analysis["revenue"]
    * 100
)

print("\n" + "=" * 60)
print("CATEGORY PERFORMANCE")
print("=" * 60)

print(category_analysis.round(2))


# ============================================================
# 10. REGIONAL PERFORMANCE
# ============================================================

region_analysis = (
    df.groupby("region_name")
    .agg(
        revenue=("revenue", "sum"),
        cost=("cost", "sum"),
        profit=("profit", "sum"),
        orders=("order_id", "nunique")
    )
)

region_analysis["profit_margin"] = (
    region_analysis["profit"]
    / region_analysis["revenue"]
    * 100
)

print("\n" + "=" * 60)
print("REGIONAL PERFORMANCE")
print("=" * 60)

print(region_analysis.round(2))


# ============================================================
# 11. CUSTOMER SEGMENT PERFORMANCE
# ============================================================

segment_analysis = (
    df.groupby("segment")
    .agg(
        revenue=("revenue", "sum"),
        cost=("cost", "sum"),
        profit=("profit", "sum"),
        orders=("order_id", "nunique"),
        customers=("customer_id", "nunique")
    )
)

segment_analysis["profit_margin"] = (
    segment_analysis["profit"]
    / segment_analysis["revenue"]
    * 100
)

print("\n" + "=" * 60)
print("CUSTOMER SEGMENT PERFORMANCE")
print("=" * 60)

print(segment_analysis.round(2))


# ============================================================
# 12. MONTHLY PERFORMANCE
# ============================================================

df["order_date"] = pd.to_datetime(df["order_date"])

df["month"] = df["order_date"].dt.month

monthly_analysis = (
    df.groupby("month")
    .agg(
        revenue=("revenue", "sum"),
        cost=("cost", "sum"),
        profit=("profit", "sum"),
        orders=("order_id", "nunique")
    )
)

monthly_analysis["profit_margin"] = (
    monthly_analysis["profit"]
    / monthly_analysis["revenue"]
    * 100
)

print("\n" + "=" * 60)
print("MONTHLY PERFORMANCE")
print("=" * 60)

print(monthly_analysis.round(2))


# ============================================================
# 13. DISCOUNT ANALYSIS
# ============================================================

discount_analysis = (
    df.groupby("discount")
    .agg(
        revenue=("revenue", "sum"),
        profit=("profit", "sum"),
        orders=("order_id", "nunique"),
        average_quantity=("quantity", "mean")
    )
)

discount_analysis["profit_margin"] = (
    discount_analysis["profit"]
    / discount_analysis["revenue"]
    * 100
)

print("\n" + "=" * 60)
print("DISCOUNT ANALYSIS")
print("=" * 60)

print(discount_analysis.round(2))


# ============================================================
# 14. HIGH REVENUE + LOW MARGIN PRODUCTS
# ============================================================

product_performance = (
    df.groupby("product_name")
    .agg(
        revenue=("revenue", "sum"),
        profit=("profit", "sum")
    )
)

product_performance["profit_margin"] = (
    product_performance["profit"]
    / product_performance["revenue"]
    * 100
)

high_revenue_low_margin = (
    product_performance[
        (product_performance["revenue"] > 1_000_000)
        &
        (product_performance["profit_margin"] < 20)
    ]
    .sort_values("revenue", ascending=False)
)

print("\n" + "=" * 60)
print("HIGH REVENUE + LOW MARGIN PRODUCTS")
print("=" * 60)

print(high_revenue_low_margin.round(2))


# ============================================================
# 15. SAVE ANALYSIS RESULTS FOR EXCEL
# ============================================================

output_file = "data/processed/business_analysis.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

    # Executive KPI table
    kpi_data = pd.DataFrame({
        "Metric": [
            "Total Orders",
            "Total Customers",
            "Total Products",
            "Total Revenue",
            "Total Cost",
            "Total Profit",
            "Profit Margin"
        ],
        "Value": [
            total_orders,
            total_customers,
            total_products,
            total_revenue,
            total_cost,
            total_profit,
            overall_margin
        ]
    })

    kpi_data.to_excel(
        writer,
        sheet_name="Executive KPIs",
        index=False
    )

    top_products_revenue.to_frame(
        "Revenue"
    ).to_excel(
        writer,
        sheet_name="Top Revenue Products"
    )

    top_products_profit.to_frame(
        "Profit"
    ).to_excel(
        writer,
        sheet_name="Top Profit Products"
    )

    top_margin_products.to_excel(
        writer,
        sheet_name="Top Margin Products"
    )

    top_customers_revenue.to_frame(
        "Revenue"
    ).to_excel(
        writer,
        sheet_name="Top Customers Revenue"
    )

    top_customers_profit.to_frame(
        "Profit"
    ).to_excel(
        writer,
        sheet_name="Top Customers Profit"
    )

    category_analysis.to_excel(
        writer,
        sheet_name="Category Analysis"
    )

    region_analysis.to_excel(
        writer,
        sheet_name="Region Analysis"
    )

    segment_analysis.to_excel(
        writer,
        sheet_name="Segment Analysis"
    )

    monthly_analysis.to_excel(
        writer,
        sheet_name="Monthly Analysis"
    )

    discount_analysis.to_excel(
        writer,
        sheet_name="Discount Analysis"
    )

    high_revenue_low_margin.to_excel(
        writer,
        sheet_name="High Rev Low Margin"
    )


print("\n" + "=" * 60)
print("ANALYSIS COMPLETE")
print("=" * 60)

print("Excel analysis file created:")
print(output_file)