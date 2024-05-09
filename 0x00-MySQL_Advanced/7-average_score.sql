--  average score
CREATE PROCEDURE ComputeAverageScoreForUser (
  IN user_id INT
)
BEGIN

  DECLARE average_score DECIMAL(5,2);

  -- Calculate average score using subquery
  SELECT AVG(score) AS average_score
  FROM corrections
  WHERE user_id = user_id;

  -- Update user table with average score (assuming a column exists)
  UPDATE users
  SET average_score = average_score
  WHERE id = user_id
  AND average_score IS NULL;  -- Update only if not already set 

END;
