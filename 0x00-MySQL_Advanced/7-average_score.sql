--  average score
CREATE PROCEDURE ComputeAverageScoreForUser (
  IN user_id INT
)
BEGIN

  DECLARE average_score DECIMAL(5,2);

  SELECT AVG(score) AS average_score
  FROM corrections
  WHERE user_id = user_id;

  UPDATE users
  SET average_score = average_score
  WHERE id = user_id
  AND average_score IS NULL;

END;
