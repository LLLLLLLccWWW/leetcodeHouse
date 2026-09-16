# Write your MySQL query statement below
-- 情況 1: 屬於多個部門，選擇 primary_flag = 'Y' 者
SELECT employee_id,department_id FROM Employee WHERE primary_flag = 'Y' 
UNION
-- 情況 2: 僅屬於 1 個部門的員工
SELECT employee_id,department_id FROM Employee GROUP BY employee_id HAVING COUNT(department_id) = 1; 
