
CREATE DATABASE IF NOT EXISTS reports;

USE reports;


CREATE TABLE IF NOT EXISTS form (
  id INT AUTO_INCREMENT PRIMARY KEY,
  Fecha VARCHAR(255),
  Nombre_establecimiento VARCHAR(255),
  Direccion VARCHAR(255),
  Localidad VARCHAR(255),
  Provincia VARCHAR(255),
  Persona_contacto VARCHAR(255),
  Telefono_contacto VARCHAR(255),
  email VARCHAR(255),
  Check_Cajero VARCHAR(255),
  Check_datafono VARCHAR(255),
  CP VARCHAR(255),
  Retorno_grupo VARCHAR(255),
  comision VARCHAR(255),
  porcentaje_retorno VARCHAR(255),
  Sector_actividad VARCHAR(255),
  Aportacion_fondo_grupo VARCHAR(255),
  Metodo_reposicion_grupo VARCHAR(255),
  Fondo_inicial VARCHAR(255),
  Nombre_empresa VARCHAR(255),
  CIF VARCHAR(255),
  CP_2 VARCHAR(255),
  Direccion_Fiscal VARCHAR(255),
  Localidad_2 VARCHAR(255),
  Provincia_2 VARCHAR(255),
  Nombre_administrador VARCHAR(255),
  DNI_administrador VARCHAR(255)
);


INSERT INTO form (Fecha, Nombre_establecimiento, Direccion, Localidad, Provincia, Persona_contacto, Telefono_contacto, email, Check_Cajero, Check_datafono, CP, Retorno_grupo, comision, porcentaje_retorno, Sector_actividad, Aportacion_fondo_grupo, Metodo_reposicion_grupo, Fondo_inicial, Nombre_empresa, CIF, CP_2, Direccion_Fiscal, Localidad_2, Provincia_2, Nombre_administrador, DNI_administrador)
VALUES 
('2023-08-11', 'Establecimiento 1', 'Calle 1', 'Ciudad 1', 'Provincia 1', 'Persona 1', '111111111', 'email1@example.com', 'Sí', 'Off', '12345', 'Sí', '10%', '20', 'Sector 1', 'Cliente', 'Loomis', '5000', 'Empresa 1', 'CIF1', '54321', 'Calle 2', 'Ciudad 2', 'Provincia 2', 'Administrador 1', 'DNI1'),
('2023-08-10', 'Establecimiento 2', 'Calle 3', 'Ciudad 3', 'Provincia 3', 'Persona 2', '222222222', 'email2@example.com', 'Off', 'Sí', '67890', 'NO', '5%', '10', 'Sector 2', 'Cliente', 'Transferencia', '3000', 'Empresa 2', 'CIF2', '09876', 'Calle 4', 'Ciudad 4', 'Provincia 4', 'Administrador 2', 'DNI2'),
('2023-08-09', 'Establecimiento 3', 'Calle 5', 'Ciudad 5', 'Provincia 5', 'Persona 3', '333333333', 'email3@example.com', 'Sí', 'Sí', '13579', 'Sí', '15%', '15', 'Sector 3', 'Nosotros', 'Tarjeta', '4000', 'Empresa 3', 'CIF3', '24680', 'Calle 6', 'Ciudad 6', 'Provincia 6', 'Administrador 3', 'DNI3');


-- (Fecha)
-- (Nombre establecimiento)
-- (Dirección)
-- (Localidad)
-- (Provincia)
-- (Persona contacto)
-- (Teléfono contacto)
-- (email)
-- (Check Cajero) 
-- (Check datáfono)
-- (CP)
-- (Retorno grupo)
-- (comisión)
-- (porcentaje retorno)
-- (Sector actividad)
-- (Aportacion fondo grupo)
-- (Método reposición grupo)
-- (Fondo inicial)
-- (Nombre empresa)
-- (CIF)
-- (CP 2)
-- (Dirección Fiscal)
-- (Localidad 2)
-- (Provincia 2)
-- (Nombre administrador)
-- (DNI administrador)