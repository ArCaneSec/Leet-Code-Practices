SELECT u.product_id,
       Round(Sum(u.units * p.price) / Sum(u.units), 2) AS average_price
FROM   unitssold u
       INNER JOIN prices p
               ON u.product_id = p.product_id
                  AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP  BY u.product_id 