WITH latest_event AS (
    SELECT
        user_id,
        event_date,
        event_type,
        plan_name,
        monthly_amount,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY event_date DESC
        ) AS rn
    FROM subscription_events
),

user_stats AS (
    SELECT
        user_id,
        MAX(monthly_amount) AS max_historical_amount,
        SUM(CASE WHEN event_type = 'downgrade' THEN 1 ELSE 0 END) AS downgrade_count
    FROM subscription_events
    GROUP BY user_id
),

current_subscription AS (
    SELECT
        s.user_id,
        MAX(s.event_date) AS start_date
    FROM subscription_events s
    WHERE s.event_type = 'start'
    GROUP BY s.user_id
)

SELECT
    l.user_id,
    l.plan_name AS current_plan,
    l.monthly_amount AS current_monthly_amount,
    u.max_historical_amount,
    DATEDIFF(l.event_date, c.start_date) AS days_as_subscriber
FROM latest_event l
JOIN user_stats u
    ON l.user_id = u.user_id
JOIN current_subscription c
    ON l.user_id = c.user_id
WHERE
    l.rn = 1
    AND l.event_type <> 'cancel'
    AND u.downgrade_count > 0
    AND l.monthly_amount < u.max_historical_amount * 0.5
    AND DATEDIFF(l.event_date, c.start_date) >= 60
ORDER BY
    days_as_subscriber DESC,
    l.user_id ASC;