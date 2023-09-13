SELECT Date_format(trans_date, "%y-%m") AS month,
       country,
       Count(*)                         AS trans_count,
       Sum(CASE
             WHEN state = "approved" THEN 1
             ELSE 0
           END)                         AS approved_count,
       Sum(amount)                      AS trans_total_amount,
       Sum(CASE
             WHEN state = "approved" THEN amount
             ELSE amount = 0
           END)                         AS approved_total_amount
FROM   transactions
GROUP  BY Year(trans_date),
          Month(trans_date),
          country 