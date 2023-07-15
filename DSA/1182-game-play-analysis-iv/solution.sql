with cte as (
  select player_id, DATE_SUB(event_date, INTERVAL 1 DAY)=min(event_date) over(partition by player_id) as is_return from activity
  )
select round(sum(is_return)/count(distinct player_id), 2)  as fraction from cte
