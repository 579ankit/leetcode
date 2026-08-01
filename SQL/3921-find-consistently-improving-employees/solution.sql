WITH cte1 AS (
    SELECT
        e.employee_id,
        e.name,
        pr.rating,
        ROW_NUMBER() OVER (
            PARTITION BY e.employee_id
            ORDER BY pr.review_date DESC
        ) AS rnk
    FROM employees e
    JOIN performance_reviews pr
        ON e.employee_id = pr.employee_id
),

cte2 AS (
    SELECT
        employee_id,
        name,
        MAX(CASE WHEN rnk = 1 THEN rating END) AS latest_rating,
        MAX(CASE WHEN rnk = 2 THEN rating END) AS middle_rating,
        MAX(CASE WHEN rnk = 3 THEN rating END) AS oldest_rating,
        COUNT(*) AS review_count
    FROM cte1
    WHERE rnk <= 3
    GROUP BY employee_id, name
)

SELECT
    employee_id,
    name,
    latest_rating - oldest_rating AS improvement_score
FROM cte2
WHERE
    review_count = 3
    AND latest_rating > middle_rating
    AND middle_rating > oldest_rating
ORDER BY
    improvement_score DESC,
    name ASC;