-- Stored procedure that computes average weighted score
-- for user
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
DECLARE v_done INT DEFAULT FALSE;
DECLARE v_id INT;
DECLARE cur1 CURSOR FOR SELECT id FROM users;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = TRUE;

OPEN cur1;

read_loop: LOOP
	FETCH cur1 INTO v_id;
        IF v_done THEN
          LEAVE read_loop;
        END IF;

	SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
	INTO @weightedAvg, @summedScale
	FROM corrections
	INNER JOIN projects
	ON projects.id = corrections.project_id
	WHERE corrections.user_id = v_id;

	UPDATE users
	SET average_score = (@weightedAvg/@summedScale)
	WHERE id = v_id;

END LOOP;
CLOSE cur1;
END $$
