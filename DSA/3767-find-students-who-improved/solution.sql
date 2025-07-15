with ranked_scores as
(
    select *,row_number() over(partition by student_id,subject order by exam_date asc) as fs,
    row_number() over(partition by student_id,subject order by exam_date desc) as ls
    from scores
)
SELECT 
  s1.student_id,
  s1.subject,
  s1.score AS first_score,
  s2.score AS latest_score
FROM ranked_scores s1
JOIN ranked_scores s2 
  ON s1.student_id = s2.student_id 
  AND s1.subject = s2.subject
WHERE s1.fs = 1
  AND s2.ls = 1
  AND s2.score > s1.score
ORDER BY s1.student_id, s1.subject;
