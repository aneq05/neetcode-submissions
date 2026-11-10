-- Write your query below
SELECT E.left_operand, E.operator, E.right_operand, 
    CASE 
        WHEN E.operator = '>' AND VL.value > VR.value THEN 'true'
        WHEN E.operator = '<' AND VL.value < VR.value THEN 'true'
        WHEN E.operator = '=' AND VL.value = VR.value THEN 'true'
    ELSE 'false'
    END AS value
FROM expressions E  
    INNER JOIN variables VL  
        ON VL.name = E.left_operand
    INNER JOIN variables VR
        ON VR.name = E.right_operand;