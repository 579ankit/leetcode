with cte1 as(
    select
        b.book_id,
        b.title,
        b.author,
        b.genre,
        b.pages,
        count(*) as total_sessions,
        MAX(r.session_rating) AS highest_rating,
        MIN(r.session_rating) AS lowest_rating,
        sum(case
                when r.session_rating>=4 
                OR r.session_rating <= 2
                then 1 else 0
        end) as extreme_count 
    from books b
    join reading_sessions r
    on b.book_id=r.book_id
    group by b.book_id
    having total_sessions>=5
)
select 
    book_id,
    title,
    author,
    genre,
    pages,
    highest_rating-lowest_rating as rating_spread,
    round(extreme_count*1.0/total_sessions,2) as polarization_score 
from cte1
where 
    highest_rating>=4
and lowest_rating<=2
and round(extreme_count*1.0/total_sessions,2)>=0.6
order by
    polarization_score desc,
    title desc;
