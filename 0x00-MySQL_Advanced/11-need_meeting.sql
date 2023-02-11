-- View that shows all student names where
-- Their score is under(strict) 80
-- AND no last_meeting date OR more than a month
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS SELECT name FROM students
WHERE (score < 80 AND ((last_meeting IS NULL) OR ((CURDATE() - last_meeting) > 1)));