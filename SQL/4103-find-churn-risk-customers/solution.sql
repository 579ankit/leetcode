with latest AS (
    SELECT
        user_id,
        event_type,
        event_date,
        plan_name,
        monthly_amount,
        ROW_NUMBER() OVER(
            PARTITION BY user_id
            ORDER BY event_date DESC
        ) AS rn
    FROM subscription_events
),
agg AS (
    SELECT
        user_id,
        MAX(monthly_amount) AS max_historical_amount,
        SUM(
            CASE
                WHEN event_type = 'downgrade' THEN 1
                ELSE 0
            END
        ) AS downgrade_count,
        DATEDIFF(MAX(event_date), MIN(event_date)) AS days_as_subscriber
    FROM subscription_events
    GROUP BY user_id
)
SELECT
    l.user_id,
    l.plan_name AS current_plan,
    l.monthly_amount AS current_monthly_amount,
    a.max_historical_amount,
    a.days_as_subscriber
FROM latest l
JOIN agg a
ON l.user_id = a.user_id
WHERE
    l.rn = 1
    AND l.event_type != 'cancel'
    AND a.downgrade_count >= 1
    AND l.monthly_amount < a.max_historical_amount * 0.5
    AND a.days_as_subscriber >= 60
ORDER BY
    a.days_as_subscriber DESC,
    l.user_id ASC;