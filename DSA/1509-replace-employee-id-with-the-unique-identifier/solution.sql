select e2.unique_id ,e1.name from
employees e1 left join EmployeeUNI e2
using(id) 
