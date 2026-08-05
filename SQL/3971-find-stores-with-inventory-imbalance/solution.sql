with cte1 as(
    select
        s.store_id,
        s.store_name,
        s.location,
        i.product_name,
        i.price,
        i.quantity,
        COUNT(*) OVER(PARTITION BY i.store_id) AS cnt,
        row_number() over(partition by i.store_id order by price desc) as max_rank,
        row_number() over(partition by i.store_id order by price asc) as min_rank
    from stores s
    join inventory i
    on s.store_id=i.store_id
),
cte2 as(
    select
        store_id,
        store_name,
        location,
        MAX(CASE WHEN max_rank = 1 THEN product_name END) AS most_exp_product,
        MAX(CASE WHEN min_rank = 1 THEN product_name END) AS cheapest_product,
        MAX(CASE WHEN max_rank = 1 THEN quantity END) AS most_exp_product_quantity,
        MAX(CASE WHEN min_rank = 1 THEN quantity END) AS cheapest_product_quantity      
    from cte1
    where cnt>=3
    group by store_id
)

select 
    store_id,
    store_name,
    location,
    most_exp_product,
    cheapest_product,
    round(cheapest_product_quantity/most_exp_product_quantity,2) as imbalance_ratio
from cte2
where most_exp_product_quantity<cheapest_product_quantity
order by 
    imbalance_ratio desc,
    store_name asc;