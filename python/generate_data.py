import pandas as pd
import random

# -------------------------
# 1. Create Regions
# -------------------------

regions = [
    [1, "North"],
    [2, "South"],
    [3, "East"],
    [4, "West"]
]

regions_df = pd.DataFrame(
    regions,
    columns=["region_id", "region_name"]
)

print("REGIONS")
print(regions_df)


# -------------------------
# 2. Create Customers
# -------------------------

first_names = [
    "Rahul", "Priya", "Amit", "Neha", "Rohit",
    "Anjali", "Vikas", "Pooja", "Arjun", "Sneha"
]

last_names = [
    "Sharma", "Singh", "Verma", "Patel", "Kumar",
    "Gupta", "Mehta", "Joshi", "Yadav", "Mishra"
]

segments = [
    "Consumer",
    "Corporate",
    "Home Office"
]

cities_by_region = {
    1: ["Delhi", "Jaipur", "Chandigarh"],
    2: ["Bengaluru", "Chennai", "Hyderabad"],
    3: ["Kolkata", "Bhubaneswar", "Patna"],
    4: ["Mumbai", "Ahmedabad", "Pune"]
}


customers = []

for customer_id in range(101, 601):

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    customer_name = first_name + " " + last_name

    segment = random.choice(segments)
    region_id = random.randint(1, 4)
    city = random.choice(cities_by_region[region_id])

    customers.append([
        customer_id,
        customer_name,
        segment,
        city,
        region_id
    ])


customers_df = pd.DataFrame(
    customers,
    columns=[
        "customer_id",
        "customer_name",
        "segment",
        "city",
        "region_id"
    ]
)

print("\nCUSTOMERS")
print(customers_df.head(10))

print("\nNumber of customers:", len(customers_df))
regions_df.to_csv("data/raw/regions.csv", index=False)
customers_df.to_csv("data/raw/customers.csv", index=False)

print("\nCSV files created successfully!")

# -------------------------
# 3. Create Products
# -------------------------

# Product templates
# Product templates
product_templates = [

    # TECHNOLOGY — COMPUTERS
    ["Laptop Pro 14", "Technology", "Computers", 55000],
    ["Laptop Air 13", "Technology", "Computers", 45000],
    ["Laptop Business 15", "Technology", "Computers", 48000],
    ["Laptop Creator 16", "Technology", "Computers", 65000],
    ["Laptop Gaming 15", "Technology", "Computers", 70000],
    ["Laptop Student 14", "Technology", "Computers", 38000],
    ["Desktop Business PC", "Technology", "Computers", 40000],
    ["Desktop Pro PC", "Technology", "Computers", 60000],
    ["Desktop Compact PC", "Technology", "Computers", 35000],
    ["Workstation Pro", "Technology", "Computers", 85000],
    ["24-inch Monitor", "Technology", "Computers", 12000],
    ["27-inch Monitor", "Technology", "Computers", 18000],
    ["32-inch Monitor", "Technology", "Computers", 28000],
    ["UltraWide Monitor", "Technology", "Computers", 32000],
    ["4K Professional Monitor", "Technology", "Computers", 40000],

    # TECHNOLOGY — ACCESSORIES
    ["Wireless Mouse", "Technology", "Accessories", 700],
    ["Ergonomic Wireless Mouse", "Technology", "Accessories", 1200],
    ["Mechanical Keyboard", "Technology", "Accessories", 2500],
    ["USB Keyboard", "Technology", "Accessories", 1200],
    ["Wireless Keyboard", "Technology", "Accessories", 1800],
    ["Wireless Headphones", "Technology", "Accessories", 3500],
    ["Noise Cancelling Headphones", "Technology", "Accessories", 6500],
    ["Webcam HD", "Technology", "Accessories", 2200],
    ["Webcam Full HD", "Technology", "Accessories", 3500],
    ["USB-C Hub", "Technology", "Accessories", 1800],
    ["USB-C Docking Station", "Technology", "Accessories", 5500],
    ["External SSD 1TB", "Technology", "Accessories", 6500],
    ["External SSD 2TB", "Technology", "Accessories", 11000],
    ["Laptop Stand", "Technology", "Accessories", 1800],
    ["Premium Laptop Stand", "Technology", "Accessories", 3000],

    # TECHNOLOGY — PRINTERS
    ["Inkjet Printer", "Technology", "Printers", 8000],
    ["Laser Printer", "Technology", "Printers", 15000],
    ["Office Laser Printer", "Technology", "Printers", 25000],
    ["Color Laser Printer", "Technology", "Printers", 30000],
    ["Document Scanner", "Technology", "Printers", 12000],
    ["High Speed Scanner", "Technology", "Printers", 22000],
    ["All-in-One Printer", "Technology", "Printers", 18000],
    ["Business Multifunction Printer", "Technology", "Printers", 35000],

    # FURNITURE — CHAIRS
    ["Ergonomic Office Chair", "Furniture", "Chairs", 8000],
    ["Executive Office Chair", "Furniture", "Chairs", 15000],
    ["Visitor Chair", "Furniture", "Chairs", 3500],
    ["Mesh Office Chair", "Furniture", "Chairs", 6500],
    ["High Back Office Chair", "Furniture", "Chairs", 9500],
    ["Leather Executive Chair", "Furniture", "Chairs", 18000],
    ["Adjustable Task Chair", "Furniture", "Chairs", 7500],
    ["Conference Chair", "Furniture", "Chairs", 5000],

    # FURNITURE — TABLES
    ["Study Table", "Furniture", "Tables", 5000],
    ["Office Desk", "Furniture", "Tables", 10000],
    ["Executive Desk", "Furniture", "Tables", 18000],
    ["Computer Table", "Furniture", "Tables", 7500],
    ["Compact Office Desk", "Furniture", "Tables", 8500],
    ["L-Shaped Office Desk", "Furniture", "Tables", 16000],
    ["Conference Table", "Furniture", "Tables", 25000],
    ["Standing Desk", "Furniture", "Tables", 22000],

    # FURNITURE — STORAGE
    ["Bookshelf", "Furniture", "Storage", 6000],
    ["Filing Cabinet", "Furniture", "Storage", 9000],
    ["Office Storage Cabinet", "Furniture", "Storage", 12000],
    ["Document Rack", "Furniture", "Storage", 2500],
    ["Wooden Filing Cabinet", "Furniture", "Storage", 11000],
    ["Metal Storage Cabinet", "Furniture", "Storage", 14000],
    ["Mobile Pedestal", "Furniture", "Storage", 7000],
    ["Office Bookshelf Pro", "Furniture", "Storage", 9500],

    # OFFICE SUPPLIES — PAPER
    ["A4 Paper Pack", "Office Supplies", "Paper", 250],
    ["Premium Paper Pack", "Office Supplies", "Paper", 450],
    ["Sticky Notes Pack", "Office Supplies", "Paper", 150],
    ["Notebook Pack", "Office Supplies", "Paper", 300],
    ["Premium Notebook", "Office Supplies", "Paper", 500],
    ["A3 Paper Pack", "Office Supplies", "Paper", 400],
    ["Colored Paper Pack", "Office Supplies", "Paper", 350],
    ["Printing Paper Box", "Office Supplies", "Paper", 2200],

    # OFFICE SUPPLIES — WRITING
    ["Ball Pen Pack", "Office Supplies", "Writing", 120],
    ["Gel Pen Pack", "Office Supplies", "Writing", 180],
    ["Marker Set", "Office Supplies", "Writing", 250],
    ["Highlighter Set", "Office Supplies", "Writing", 220],
    ["Premium Ball Pen Set", "Office Supplies", "Writing", 350],
    ["Permanent Marker Pack", "Office Supplies", "Writing", 300],
    ["Whiteboard Marker Set", "Office Supplies", "Writing", 280],
    ["Professional Writing Kit", "Office Supplies", "Writing", 600],

    # OFFICE SUPPLIES — STORAGE
    ["File Folder Pack", "Office Supplies", "Storage", 300],
    ["Document Folder", "Office Supplies", "Storage", 180],
    ["Desk Organizer", "Office Supplies", "Storage", 500],
    ["Archive Box", "Office Supplies", "Storage", 400],
    ["Premium File Organizer", "Office Supplies", "Storage", 750],
    ["Document Storage Box", "Office Supplies", "Storage", 600],
    ["Expandable File Folder", "Office Supplies", "Storage", 450],
    ["Desktop File Holder", "Office Supplies", "Storage", 550],

    # OFFICE SUPPLIES — DESK ACCESSORIES
    ["Calculator", "Office Supplies", "Desk Accessories", 500],
    ["Scientific Calculator", "Office Supplies", "Desk Accessories", 900],
    ["Desk Calendar", "Office Supplies", "Desk Accessories", 250],
    ["Desk Stapler", "Office Supplies", "Desk Accessories", 180],
    ["Heavy Duty Stapler", "Office Supplies", "Desk Accessories", 450],
    ["Paper Punch", "Office Supplies", "Desk Accessories", 220],
    ["Desk Tape Dispenser", "Office Supplies", "Desk Accessories", 150],
    ["Letter Tray", "Office Supplies", "Desk Accessories", 350],
    ["Laptop Privacy Screen", "Technology", "Accessories", 2500],
["Bluetooth Speaker", "Technology", "Accessories", 2800],
["Portable SSD 500GB", "Technology", "Accessories", 4000],
["Printer Stand", "Furniture", "Storage", 3000],
["Cable Management Box", "Office Supplies", "Desk Accessories", 450],
["Desktop Whiteboard", "Office Supplies", "Desk Accessories", 700]
]

products = []

for product_id in range(501, 601):

    template = product_templates[product_id - 501]

    product_name = template[0]
    category = template[1]
    sub_category = template[2]
    cost_price = template[3]

    products.append([
        product_id,
        product_name,
        category,
        sub_category,
        cost_price
    ])


products_df = pd.DataFrame(
    products,
    columns=[
        "product_id",
        "product_name",
        "category",
        "sub_category",
        "cost_price"
    ]
)

print("\nPRODUCTS")
print(products_df.head(10))

print("\nNumber of products:", len(products_df))

products_df.to_csv(
    "data/raw/products.csv",
    index=False
)

print("\nProducts CSV created successfully!")
# -------------------------
# 4. Create Orders
# -------------------------

orders = []

for order_id in range(10001, 20001):

    order_date = pd.Timestamp(
        "2025-01-01"
    ) + pd.to_timedelta(
        random.randint(0, 364),
        unit="D"
    )

    customer_id = random.randint(101, 600)

    product_id = random.randint(501, 600)

    quantity = random.randint(1, 5)

    # Find the selected product
    product = products_df[
        products_df["product_id"] == product_id
    ].iloc[0]

    cost_price = product["cost_price"]

    # Selling price is 20% to 60% higher than cost
    markup = random.uniform(1.20, 1.60)

    selling_price = round(
        cost_price * markup,
        2
    )

    # Discount between 0% and 20%
    discount = round(
        random.uniform(0, 0.20),
        2
    )

    orders.append([
        order_id,
        order_date.date(),
        customer_id,
        product_id,
        quantity,
        selling_price,
        discount
    ])


orders_df = pd.DataFrame(
    orders,
    columns=[
        "order_id",
        "order_date",
        "customer_id",
        "product_id",
        "quantity",
        "selling_price",
        "discount"
    ]
)

print("\nORDERS")
print(orders_df.head(10))

print("\nNumber of orders:", len(orders_df))

orders_df.to_csv(
    "data/raw/orders.csv",
    index=False
)

print("\nOrders CSV created successfully!")

# -------------------------
# 5. Validate the Data
# -------------------------

print("\n========================")
print("DATA VALIDATION")
print("========================")

# Check number of rows
print("Customers:", len(customers_df))
print("Products:", len(products_df))
print("Orders:", len(orders_df))

# Check missing values
print("\nMissing values:")
print("Customers:", customers_df.isnull().sum().sum())
print("Products:", products_df.isnull().sum().sum())
print("Orders:", orders_df.isnull().sum().sum())

# Check duplicate IDs
print("\nDuplicate IDs:")
print(
    "Customer IDs:",
    customers_df["customer_id"].duplicated().sum()
)

print(
    "Product IDs:",
    products_df["product_id"].duplicated().sum()
)

print(
    "Order IDs:",
    orders_df["order_id"].duplicated().sum()
)

# Check quantity
print("\nQuantity range:")
print(
    orders_df["quantity"].min(),
    "to",
    orders_df["quantity"].max()
)

# Check discount
print("\nDiscount range:")
print(
    orders_df["discount"].min(),
    "to",
    orders_df["discount"].max()
)