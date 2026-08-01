with cte1 as(
    select 
        d.driver_id,
        d.driver_name,
        AVG(CASE WHEN MONTH(t.trip_date) BETWEEN 1 AND 6
            THEN t.distance_km / t.fuel_consumed END) as first_half_avg,
        AVG(CASE WHEN MONTH(t.trip_date) BETWEEN 7 AND 12
            THEN t.distance_km / t.fuel_consumed END) as second_half_avg
    from drivers d
    join trips t
    on d.driver_id=t.driver_id
    group by 
        d.driver_id,
        d.driver_name
)
select 
    driver_id,
    driver_name,
    round(first_half_avg,2) as first_half_avg,
    round(second_half_avg,2) as second_half_avg,
    round(second_half_avg-first_half_avg,2) as efficiency_improvement 
from cte1
where 
    first_half_avg is not null
and second_half_avg is not null
AND second_half_avg > first_half_avg
order by 
    efficiency_improvement desc,
    driver_name asc;