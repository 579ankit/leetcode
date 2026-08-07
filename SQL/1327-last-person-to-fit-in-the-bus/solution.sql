with cte as(
    select
        person_name,
        weight,
        sum(weight) over(order by turn asc) as total_weight,
        row_number() over(order by turn asc) as rnk
    from queue
)

select
    person_name
from cte
where 
    total_weight<=1000
order by rnk desc 
limit 1;