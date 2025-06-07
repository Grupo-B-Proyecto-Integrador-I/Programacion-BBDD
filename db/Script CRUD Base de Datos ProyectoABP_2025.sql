USE `ProyectoABP_2025`;
DELETE FROM User WHERE user_name IN ('admin_test', 'user_test');

INSERT INTO User (rol_id, user_name, user_password) VALUES 
((SELECT rol_id FROM Rol WHERE rol_name = 'admin'), 'admin_test', 'hash_admin_123'), 
((SELECT rol_id FROM Rol WHERE rol_name = 'user'), 'user_test', 'hash_user_abc');

SELECT U.user_id, U.user_name, R.rol_name
FROM User U 
INNER JOIN Rol R ON U.rol_id = R.rol_id; 

SELECT user_id, user_name, rol_id 
FROM User 
WHERE user_name = 'admin_test';
 
SELECT user_name, rol_id 
FROM User 
WHERE user_id = 1; 

UPDATE User 
SET user_password = 'nuevo_hash_de_user_test' 
WHERE user_name = 'user_test'; 

UPDATE User 
SET rol_id = (SELECT rol_id FROM Rol WHERE rol_name = 'admin') 
WHERE user_name = 'user_test';

DELETE FROM User 
WHERE user_name = 'user_test'; 

DELETE FROM User WHERE user_id = 2;