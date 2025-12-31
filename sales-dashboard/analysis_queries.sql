-- 1. Total Revenue by Region
SELECT 
    region, 
    SUM(amount) as total_revenue 
FROM sales 
GROUP BY region 
ORDER BY total_revenue DESC;

-- 2. Monthly Sales Trend
SELECT 
    strftime('%Y-%m', date) as month, 
    SUM(amount) as monthly_sales 
FROM sales 
GROUP BY month;

-- 3. Top Performing Categories
SELECT 
    category, 
    COUNT(order_id) as total_orders, 
    AVG(amount) as avg_order_value 
FROM sales 
GROUP BY category;