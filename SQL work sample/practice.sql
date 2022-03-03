SELECT student_id, sum(marks) as SUM_OF_MARKS
FROM marks 
GROUP BY student_id
ORDER BY student_id DESC

-- count duplicate name
SELECT name, COUNT(CONCAT(name, phone, age)) as cnt
GROUP BY name
HAVING cnt > 1


-- UNION
SELECT * 
FROM (SELECT DISTINCT city, LENGTH(city) 
	FROM station 
	ORDER BY LENGTH(city) ASC, city ASC
	) 
LIMIT 1

UNION

SELECT * 
FROM 
	(SELECT DISTINCT city, LENGTH(city) 
		FROM station 
		ORDER BY LENGTH(city) DESC, city ASC) 
LIMIT 1
