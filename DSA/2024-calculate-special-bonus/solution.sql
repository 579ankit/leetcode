select employee_id,
case
when employee_id %2 !=0 and name not like 'M%' then salary
when employee_id %2 !=0 and name like 'M%' then salary = 0
when employee_id %2 =0 then salary = 0
end as bonus
from  employees order by employee_id
