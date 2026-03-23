-- SQLite
-- 1. Total Customers
SELECT COUNT(*) FROM customers;

-- 2. Churn Distribution
SELECT Churn, COUNT(*) 
FROM customers
GROUP BY Churn;

-- 3. Create Enriched Table
CREATE TABLE customers_enriched AS
SELECT *,
CASE 
    WHEN tenure <= 12 THEN '0-1 Year'
    WHEN tenure <= 24 THEN '1-2 Years'
    ELSE '2+ Years'
END AS tenure_group
FROM customers;

-- 4. Churn Rate
SELECT 
COUNT(*) total,
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*) churn_rate
FROM customers_enriched;