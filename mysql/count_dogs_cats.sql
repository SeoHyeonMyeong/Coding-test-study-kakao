-- 고양이와 개는 몇 마리 있을까
SELECT animal_type, COUNT(animal_id) AS "count"
FROM animal_ins
WHERE animal_type IN('Cat','Dog')
GROUP BY animal_type
ORDER BY animal_type ASC ;