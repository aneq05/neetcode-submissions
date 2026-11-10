-- Write your query below
SELECT DISTINCT ON (student_id) student_id, exam_id, score
FROM exam_results
-- najwyższy score -> DESC
-- najmniejszy exam_id -> ASC
ORDER BY student_id, score DESC, exam_id ASC;
