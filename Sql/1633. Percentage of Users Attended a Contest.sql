SELECT contest_id,
       Round(Count(*) / (SELECT Count(*)
                         FROM   users) * 100, 2) AS percentage
FROM   register r
GROUP  BY contest_id
ORDER  BY percentage DESC,
          contest_id ASC 