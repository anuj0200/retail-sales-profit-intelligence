# Retail Sales & Profit Intelligence System

An end-to-end Business Analytics project that transforms retail transaction data into actionable business insights using Python, MySQL, SQL, and Excel.

## 📊 Project Overview

The goal of this project was to analyze retail sales and profitability and identify opportunities for improving business performance.

The project follows this workflow:

Raw Data → Python → MySQL → SQL Analysis → Excel Dashboard → Business Insights

## 🎯 Business Questions

The analysis answers questions such as:

- How much revenue and profit did the business generate?
- Which products generate the most revenue?
- Which products generate the most profit?
- Which regions and customer segments perform best?
- How does discounting affect profit margins?
- Which high-revenue products have below-average margins?

## 📁 Dataset

The dataset contains:

- 10,000 orders
- 500 customers
- 100 products
- 4 regions
- Multiple customer segments
- Product categories
- Order dates
- Quantity
- Selling price
- Discount
- Product cost

> Note: The dataset is synthetic and was generated for portfolio and analytical demonstration purposes.

## 🛠️ Technology Stack

### Python
- Pandas
- NumPy
- Data generation
- Data validation
- Data processing

### MySQL
- Database management
- SQL queries
- JOINs
- GROUP BY
- Aggregations
- HAVING
- Business KPI analysis

### Excel
- KPI dashboard
- Data visualization
- Trend analysis
- Product analysis
- Regional analysis
- Discount analysis

## 📈 Key KPIs

| Metric | Result |
|---|---:|
| Total Orders | 10,000 |
| Total Customers | 500 |
| Total Products | 100 |
| Total Revenue | ₹45.02 Cr |
| Total Profit | ₹9.28 Cr |
| Profit Margin | 20.61% |

## 💡 Key Business Insights

### 1. Strong overall profitability

The business generated approximately ₹45.02 Cr in revenue and ₹9.28 Cr in profit, resulting in an overall profit margin of 20.61%.

### 2. Workstation Pro is the leading revenue product

Workstation Pro generated approximately ₹4.16 Cr in revenue, making it the highest-revenue product.

### 3. High-revenue products with below-average margins

Several high-revenue products operate below the overall 20.61% profit margin.

Examples include:

- Laptop Air 13 — 19.07%
- Laptop Student 14 — 19.12%
- Desktop Compact PC — 18.58%

These products represent potential opportunities for pricing, discount, or cost optimization.

### 4. Discounting is associated with lower profitability

Profit margin decreases substantially as discount levels increase.

The observed margin decreases from:

- 28.90% at 0% discount
- 21.49% at 10% discount
- 9.75% at 20% discount

This suggests that discount strategies should be carefully managed to protect profitability.

### 5. Regional and category performance varies

The analysis compares revenue, profit, order volume, and profit margin across regions and product categories to identify stronger and weaker business areas.

## 📊 Excel Dashboard

The dashboard provides an executive-level view of:

- Total Revenue
- Total Profit
- Profit Margin
- Total Orders
- Monthly Revenue & Profit
- Top 10 Products by Revenue
- Profit by Category
- Profit by Region
- Key Business Insights

## 🔄 Project Workflow

```text
Raw CSV Data
     ↓
Python Data Generation & Validation
     ↓
MySQL Database
     ↓
SQL Business Analysis
     ↓
Excel Analysis
     ↓
Executive Dashboard
     ↓
Business Insights