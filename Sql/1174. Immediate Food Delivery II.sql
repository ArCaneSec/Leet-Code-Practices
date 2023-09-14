SELECT 
    ROUND(SUM(t.JJ) / COUNT(*) * 100,2) AS immediate_percentage
FROM
    (SELECT 
        customer_id,
            MIN(order_date),
            CASE
                WHEN MIN(order_date) = MIN(customer_pref_delivery_date) THEN 1
                ELSE 0
            END AS JJ
    FROM
        Delivery
    GROUP BY customer_id) AS t