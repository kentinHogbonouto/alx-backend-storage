-- Stored procedure that adds a new correction for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
SELECT AVG(score) INTO @average
FROM corrections
WHERE user_id = user_id;

UPDATE users
SET average_score = @average
WHERE id = user_id;
END $$
