select a.employee_id,a.name,count(b.reports_to) reports_count,round(avg(b.age),0) as average_age from employees a join employees b on a.employee_id=b.reports_to group by b.reports_to order by a.employee_id


