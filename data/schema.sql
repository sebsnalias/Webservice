create database ferreteria_jvt;
use ferreteria_jvt;

create table clientes(
    id_cliente  INT AUTO_INCREMENT PRIMARY KEY,
    nombre_cliente  VARCHAR(50) NOT NULL,
    apellido_paterno_cliente    VARCHAR(50) NOT NULL,
    apellido_materno_cliente    VARCHAR(50) NOT NULL,
    telefono_cliente    VARCHAR(10) NOT NULL,
    email_cliente   VARCHAR(100)    NOT NULL);

insert into clientes(nombre_cliente, apellido_paterno_cliente, apellido_materno_cliente, telefono_cliente, email_cliente) values
    ('Rogelio', 'Tellez', 'Cercas', '7751432189', 'Roger21@gmail.com'),
    ('Paul', 'Aguilar', 'Resendiz', '7751341021', 'paul32@gmail.com'),
    ('Elena', 'Islas', 'Sosa', '7751098021', 'nitta_flor@gmail.com');

CREATE USER 'Jonatan2019' IDENTIFIED BY '1996kuorra';
GRANT USAGE ON *.* TO 'Jonatan2019'@localhost IDENTIFIED BY '1998kuorra';
GRANT ALL privileges ON `ferreteria_jvt`.* TO 'Jonatan2019'@localhost;
FLUSH PRIVILEGES;