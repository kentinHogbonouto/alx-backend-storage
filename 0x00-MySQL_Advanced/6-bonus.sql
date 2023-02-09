-- Stored procedure that adds a new correction for a student
DELIMITER $$
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score FLOAT)
BEGIN
IF EXISTS(SELECT * from projects WHERE name=project_name) = 0
	THEN INSERT INTO projects (name) VALUES (project_name);
	SET @project_id = LAST_INSERT_ID();
ELSE
	SELECT id INTO @project_id FROM projects WHERE name=project_name;
END IF;
INSERT INTO corrections(user_id, project_id, score) VALUES (user_id, @project_id, score);
END $$
