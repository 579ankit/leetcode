with cte1 as(
    select
        u.name,
        count(mr.rating) as count_rating
    from users u
    join movierating mr
    on u.user_id=mr.user_id
    group by 
        u.user_id,
        u.name
    order by    
        count_rating desc,
        name asc
    limit 1
),
cte2 as(
    select
        m.title,
        avg(mr.rating) as average_rating
    from movies m
    join movierating mr
    on m.movie_id=mr.movie_id
    where mr.created_at between '2020-02-01' and '2020-02-29'
    group by
        m.movie_id,
        m.title
    order by
        average_rating desc,
        title asc
    limit 1
)
select name as results from cte1
union all
select title as results from cte2;
