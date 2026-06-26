select ifnull(e2.unique_id,null) as unique_id,e1.name 
from employees e1 left join employeeuni e2
on e1.id=e2.id;
