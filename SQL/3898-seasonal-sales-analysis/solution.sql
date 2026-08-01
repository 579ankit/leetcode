with cte as(
    select
        CASE 
        WHEN month(s.sale_date)=09 or month(s.sale_date)=10 or month(s.sale_date)=11 then 'Fall'
        WHEN month(s.sale_date)=06 or month(s.sale_date)=07 or month(s.sale_date)=08 then 'Summer' 
        WHEN month(s.sale_date)=03 or month(s.sale_date)=04 or month(s.sale_date)=05 then 'Spring' 
        WHEN month(s.sale_date)=12 or month(s.sale_date)=01 or month(s.sale_date)=02 then 'Winter' 
        end as season,
        p.category,
        sum(s.quantity) as total_quantity,
        sum(s.quantity*s.price) as total_revenue,
        dense_rank() over(partition by 
                CASE
                    WHEN MONTH(s.sale_date) IN (9,10,11) THEN 'Fall'
                    WHEN MONTH(s.sale_date) IN (6,7,8) THEN 'Summer'
                    WHEN MONTH(s.sale_date) IN (3,4,5) THEN 'Spring'
                    ELSE 'Winter'
                END
            order by
                SUM(s.quantity) DESC,
                SUM(s.quantity * s.price) DESC,
                p.category ASC) as rnk
    from sales s
    join products p
    on s.product_id=p.product_id
    group by 
        season,
        p.category
)

select 
    season,
    category,
    sum(total_quantity) as total_quantity,
    sum(total_revenue) as total_revenue
from cte
where rnk=1
group by 
    season,
    category
order by season
