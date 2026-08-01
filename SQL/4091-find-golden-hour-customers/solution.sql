with cte as(
    select
        customer_id,
        count(*) as total_orders,
        sum(
            case when 
                time(order_timestamp) between '11:00' and '14:00' or 
                time(order_timestamp) between '18:00' and '21:00'
                then 1 else 0
            end 
        ) as peak_hours,
        sum(order_rating) as sum_order_rating,
        count(order_rating) as count_order_rating
    from restaurant_orders
    group by customer_id
)
select 
    customer_id,
    total_orders,
    round(peak_hours*100.0/total_orders,0) as peak_hour_percentage,
    round(sum_order_rating/count_order_rating,2) as average_rating
from cte 
WHERE total_orders >= 3
  AND peak_hours * 1.0 / total_orders >= 0.6
  AND sum_order_rating * 1.0 / count_order_rating >= 4.0
  AND count_order_rating * 1.0 / total_orders >= 0.5
order by
    average_rating desc,
    customer_id desc;