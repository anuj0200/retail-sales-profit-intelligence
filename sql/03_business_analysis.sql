-- ============================================
-- Retail Sales & Profit Intelligence System
-- Business Analysis Queries
-- ============================================

USE retail_intelligence;


-- 1. TOTAL REVENUE
SELECT
    ROUND(
        SUM(quantity * selling_price * (1 - discount)),
        2
    ) AS total_revenue
FROM orders;


-- 2. TOTAL PROFIT
SELECT
    ROUND(
        SUM(
            o.quantity * o.selling_price * (1 - o.discount)
            - o.quantity * p.cost_price
        ),
        2
    ) AS total_profit
FROM orders o
JOIN products p
    ON o.product_id = p.product_id;


-- 3. OVERALL PROFIT MARGIN
SELECT
    ROUND(
        SUM(
            o.quantity * o.selling_price * (1 - o.discount)
            - o.quantity * p.cost_price
        )
        /
        SUM(
            o.quantity * o.selling_price * (1 - o.discount)
        ) * 100,
        2
    ) AS profit_margin
FROM orders o
JOIN products p
    ON o.product_id = p.product_id;


-- 4. TOP 10 PRODUCTS BY REVENUE
SELECT
    p.product_name,
    ROUND(
        SUM(o.quantity * o.selling_price * (1 - o.discount)),
        2
    ) AS total_revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_revenue DESC
LIMIT 10;


-- 5. HIGH-REVENUE / LOW-MARGIN PRODUCTS
SELECT
    p.product_name,

    ROUND(
        SUM(o.quantity * o.selling_price * (1 - o.discount)),
        2
    ) AS revenue,

    ROUND(
        SUM(
            o.quantity * o.selling_price * (1 - o.discount)
            - o.quantity * p.cost_price
        ),
        2
    ) AS profit,

    ROUND(
        SUM(
            o.quantity * o.selling_price * (1 - o.discount)
            - o.quantity * p.cost_price
        )
        /
        SUM(
            o.quantity * o.selling_price * (1 - o.discount)
        ) * 100,
        2
    ) AS profit_margin

FROM orders o
JOIN products p
    ON o.product_id = p.product_id

GROUP BY p.product_name

HAVING profit_margin < 20.61

ORDER BY revenue DESC;