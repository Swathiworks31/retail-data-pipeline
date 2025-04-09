-- View 1: Top 5 Products by Revenue
CREATE OR REPLACE VIEW RETAIL_PROJECT.TRANSFORMED.VW_TOP_PRODUCTS AS
SELECT
    dp.name AS product_name,
    dp.category,
    SUM(fs.amount) AS total_revenue
FROM RETAIL_PROJECT.TRANSFORMED.FACT_SALES fs
JOIN RETAIL_PROJECT.TRANSFORMED.DIM_PRODUCTS dp
    ON fs.product_id = dp.product_id
GROUP BY dp.name, dp.category
ORDER BY total_revenue DESC
LIMIT 5;


-- View 2: Monthly Sales Trend
CREATE OR REPLACE VIEW RETAIL_PROJECT.TRANSFORMED.VW_MONTHLY_SALES AS
SELECT
    TO_CHAR(transaction_date, 'YYYY-MM') AS month,
    ROUND(SUM(amount), 2) AS total_revenue
FROM RETAIL_PROJECT.TRANSFORMED.FACT_SALES
GROUP BY TO_CHAR(transaction_date, 'YYYY-MM')
ORDER BY month;


-- View 3: Revenue by Customer Segment
CREATE OR REPLACE VIEW RETAIL_PROJECT.TRANSFORMED.VW_REVENUE_BY_SEGMENT AS
SELECT
    dc.customer_segment,
    ROUND(SUM(fs.amount), 2) AS total_revenue
FROM RETAIL_PROJECT.TRANSFORMED.FACT_SALES fs
JOIN RETAIL_PROJECT.TRANSFORMED.DIM_CUSTOMERS dc
    ON fs.customer_id = dc.customer_id
GROUP BY dc.customer_segment
ORDER BY total_revenue DESC;
