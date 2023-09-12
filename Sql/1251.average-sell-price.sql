SELECT u.product_id, round(sum( u.units * p.price ) / sum(u.units), 2) AS average_price
FROM UnitsSold u
INNER JOIN prices p ON u.product_id = p.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY u.product_id