-- Stored procedure that computes average weighted score
-- for user
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
INTO @weightedAvg, @summedScale
FROM corrections
INNER JOIN projects
ON projects.id = corrections.project_id
WHERE corrections.user_id = user_id;

UPDATE users
SET average_score = (@weightedAvg/@summedScale)
WHERE id = user_id;
END $$
