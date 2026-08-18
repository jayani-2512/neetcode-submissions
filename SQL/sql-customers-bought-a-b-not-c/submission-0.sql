SELECT customer_id, customer_name
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
    GROUP BY customer_id
    HAVING COUNT(*) FILTER (WHERE product_name = 'A') > 0
       AND COUNT(*) FILTER (WHERE product_name = 'B') > 0
       AND COUNT(*) FILTER (WHERE product_name = 'C') = 0
)
ORDER BY customer_name;