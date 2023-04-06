-- INSERTA EL NOMBRE DE TU BASE DE DATOS EN LA PARTE DE ABAJO
USE 'YOUR DATABASE';

CREATE TABLE inventario (
	id int not null auto_increment,
    sede varchar(20),
    area varchar(20),
    tipo_equipo varchar(20),
    nombre_equipo varchar(20),
    modelo varchar(50),
    tiene_monitor varchar(5),
    marca_monitor varchar(20),
    num_serie varchar(20),
    num_inventario varchar(20),
    caracteristicas_equipo varchar(50),
    usuario varchar(50),
    ip varchar(20),
    metodo_conexion varchar(20),
    bitdefender varchar(5),
    tiene_global varchar(5),
    agente_global varchar(20),
    cuenta_impresora varchar(20),
    pin_impresora varchar(5),
    no_break varchar(5),
    num_extension varchar(5),
    nombre_extension varchar(50),
    observaciones varchar(250),
    primary key (id)
);



