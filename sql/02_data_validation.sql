-- ============================================
-- Retail Sales & Profit Intelligence System
-- Data Validation Queries
-- ============================================

USE retail_intelligence;


-- 1. CHECK TOTAL ORDERS
SELECT COUNT(*) AS total_orders
FROM orders;


-- 2. CHECK TOTAL CUSTOMERS
SELECT COUNT(*) AS total_customers
FROM customers;


-- 3. CHECK TOTAL PRODUCTS
SELECT COUNT(*) AS total_products
FROM products;


-- 4. CHECK DUPLICATE ORDER IDs
SELECT
    order_id,
    COUNT(*) AS duplicate_count
FROM orders
GROUP BY order_id
HAVING COUNT(*) > 1;


-- 5. CHECK DUPLICATE CUSTOMER IDs
SELECT
    customer_id,
    COUNT(*) AS duplicate_count
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;


-- 6. CHECK DUPLICATE PRODUCT IDs
SELECT
    product_id,
    COUNT(*) AS duplicate_count
FROM products
GROUP BY product_id
HAVING COUNT(*) > 1;


-- 7. CHECK MISSING VALUES IN ORDERS
SELECT
    COUNT(*) AS missing_values
FROM orders
WHERE order_id IS NULL
   OR order_date IS NULL
   OR customer_id IS NULL
   OR product_id IS NULL
   OR quantity IS NULL
   OR selling_price IS NULL
   OR discount IS NULL;


-- 8. CHECK QUANTITY RANGE
SELECT
    MIN(quantity) AS minimum_quantity,
    MAX(quantity) AS maximum_quantity
FROM orders;


-- 9. CHECK DISCOUNT RANGE
SELECT
    MIN(discount) AS minimum_discount,
    MAX(discount) AS maximum_discount
FROM orders;