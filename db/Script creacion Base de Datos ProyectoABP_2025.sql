CREATE DATABASE IF NOT EXISTS `ProyectoABP_2025`;

USE `ProyectoABP_2025`;

CREATE TABLE `Rol` (
    `rol_id` INT PRIMARY KEY AUTO_INCREMENT,
    `rol_name` VARCHAR(50) NOT NULL UNIQUE,
    `rol_description` VARCHAR(255)
);

CREATE TABLE `User` (
    `user_id` INT PRIMARY KEY AUTO_INCREMENT,
    `rol_id` INT NOT NULL,
    `user_name` VARCHAR(100) NOT NULL UNIQUE,
    `user_password` VARCHAR(255) NOT NULL,    
    FOREIGN KEY (`rol_id`) REFERENCES `Rol`(`rol_id`)
);

INSERT INTO `Rol` (`rol_name`, `rol_description`) VALUES
('admin', 'Puede visualizar, modificar y eliminar usuarios del sistema.'),
('user', 'Puede acceder y gestionar solo sus propios datos personales.');