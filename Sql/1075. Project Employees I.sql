SELECT project_id,
       Round(Sum(experience_years) / Count(*), 2) AS average_years
FROM   employee e
       INNER JOIN project p
               ON e.employee_id = p.employee_id
GROUP  BY project_id 