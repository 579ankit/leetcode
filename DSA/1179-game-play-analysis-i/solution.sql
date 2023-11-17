SELECT PLAYER_ID,min(EVENT_DATE) AS FIRST_LOGIN from activity group by player_id 
