with cte1 as(
    select
        s.store_id,
        s.store_name,
        s.location,
        i.quantity,
        i.price,
        i.product_name,
        #count(*) as total_products,
        row_number() over(partition by i.store_id order by i.price desc) as max_rank,
        row_number() over(partition by i.store_id order by i.price asc) as min_rank
    from stores s
    join inventory i
    on s.store_id=i.store_id
),
cte2 as(
    select
        store_id,
        store_name,
        location,
        quantity,
        price,
        product_name,
        max(case when max_rank=1 then product_name end) as most_exp_product,
        min(case when min_rank=1 then product_name end) as cheapest_product,
        max(case when max_rank=1 then quantity end) as highest_quantity,
        min(case when min_rank=1 then quantity end) as lowest_quantity
    from cte1
    group by store_id
    having count(*)>=3
)
select 
    store_id,
    store_name,
    location,
    most_exp_product,
    cheapest_product,
    round(lowest_quantity/highest_quantity,2) as imbalance_ratio
from cte2
where 
    highest_quantity<lowest_quantity
order by 
    imbalance_ratio desc,
    store_name asc;