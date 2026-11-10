-- Write your query below
SELECT SP.name 
FROM sales_person SP 
WHERE NOT EXISTS (
    SELECT 1
    FROM orders O
    JOIN company C
        ON O.com_id = C.com_id
    WHERE C.name = 'CRIMSON'
    AND O.sales_id = SP.sales_id
);