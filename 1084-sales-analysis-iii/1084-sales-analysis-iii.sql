# Write your MySQL query statement below
SELECT distinct P.product_id, P.product_name
FROM Product P
INNER JOIN Sales S ON P.product_id = S.product_id
WHERE S.sale_date BETWEEN '2019-01-01' AND '2019-03-31'
  AND P.product_id NOT IN (
    SELECT P.product_id
    FROM Product P
    INNER JOIN Sales S ON P.product_id = S.product_id
    WHERE S.sale_date < '2019-01-01' OR S.sale_date > '2019-03-31'
  );
