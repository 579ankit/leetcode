with cte as
(
    select d.name department,e.name as employee,
    e.salary salary,
    dense_rank() over(partition by d.name 
    order by e.salary desc) as 'rnk'
    from employee e join department d on
    e.departmentId =d.id
)
select department,employee,salary 
from cte where rnk=1;
