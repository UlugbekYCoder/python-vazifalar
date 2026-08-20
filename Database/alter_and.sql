--1  SELECT * FROM products
-- WHERE available = TRUE AND price BETWEEN 50 AND 500 AND quantity > 5
-- ORDER BY price DESC;

--2 SELECT * FROM products
-- WHERE (price < 100.00 AND quantity > 20) OR (price >= 500 AND available)
-- ORDER BY available DESC, price DESC;

-- 3
-- SELECT name, price, description
-- FROM products
-- WHERE description IS NOT NULL
--     And description ILIKE '%phone%'
-- ORDER BY name;

-- 4
-- SELECT name, price, quantity FROM products
-- WHERE available = TRUE 
--     AND quantity > 0
-- ORDER BY price ASC
-- LIMIT 5;

-- 5
-- SELECT id,name,price,quantity FROM products
-- WHERE available = TRUE 
--     AND quantity > 0
--     AND price BETWEEN 100 and 2000
--     AND description IS NOT NULL
--     AND(name ILIKE '%Pro%' or name ILIKE '%Max%')
-- ORDER BY price DESC, quantity DESC
-- LIMIT 3;