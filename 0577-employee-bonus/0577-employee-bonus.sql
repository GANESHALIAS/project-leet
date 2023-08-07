# Write your MySQL query statement below
select E.name , B.bonus from Employee E left outer join Bonus B  on E.empid=B.empid where B.bonus<1000 or B.bonus is null;