# Write your MySQL query statement below
select E.employee_id from Employees E left join Salaries S on E.employee_id = S.employee_id where S.salary is null union select S.employee_id from Salaries S left join Employees E on S.employee_id = E.employee_id where E.name is null order by employee_id

