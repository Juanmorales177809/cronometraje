CREATE database Morron;
USE Morron;

CREATE TABLE corredores(
id bigint primary key auto_increment not null,
	Numero double not null,
    Nombre varchar(50) not null,
    Documento double not null,
    Distancia double not null,
    Puesto double not null,
    HoraSalida double not null,
    HoraMeta double not null,
    TiempoCarrera varchar(50) not null,
    Estado varchar(50) not null,
    Telefono double not null);
    


