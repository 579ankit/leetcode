WITH cte AS (
    SELECT
        user_id,
        reaction,
        COUNT(*) AS reaction_count,
        SUM(COUNT(*)) OVER(PARTITION BY user_id) AS total_count,
        DENSE_RANK() OVER(
            PARTITION BY user_id
            ORDER BY COUNT(*) DESC
        ) AS rnk
    FROM reactions
    GROUP BY user_id, reaction
)
SELECT
    user_id,
    reaction as dominant_reaction,
    ROUND(reaction_count * 1.0 / total_count, 2) AS reaction_ratio
FROM cte
WHERE rnk = 1
  AND reaction_count * 1.0 / total_count >= 0.6
  AND total_count >= 5
order by 
    reaction_ratio desc,
    user_id asc;