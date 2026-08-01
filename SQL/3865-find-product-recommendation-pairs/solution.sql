with cte1 as(
    select
        distinct
        pp1.user_id,
        pp1.product_id as product1_id,
        pp2.product_id as product2_id
        from ProductPurchases pp1
        join ProductPurchases pp2
        on pp1.user_id=pp2.user_id
        and pp1.product_id<pp2.product_id
),
cte2 as(
    select
        c1.product1_id,
        c1.product2_id,
        pi1.category as product1_category,
        pi2.category as product2_category,
        count(*) as customer_count
    from cte1 c1
    join ProductInfo pi1
    on c1.product1_id=pi1.product_id
    join ProductInfo pi2
    on c1.product2_id=pi2.product_id
    group by
        c1.product1_id,
        c1.product2_id,
        product1_category,
        product2_category
)

select 
    * 
from cte2
where customer_count>=3
order by
    customer_count desc,
    product1_id asc,
    product2_id asc;