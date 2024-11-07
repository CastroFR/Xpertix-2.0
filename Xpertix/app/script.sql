DROP DATABASE xpertix_db;
CREATE DATABASE xpertix_db;
USE xpertix_db;

-- Tabla de Usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(100) NOT NULL UNIQUE,
    correo VARCHAR(150) NOT NULL UNIQUE,
    contrasena_hash VARCHAR(200) NOT NULL,
    rol VARCHAR(50) NOT NULL, -- Roles como Desarrollador, Probador, Gerente, etc.
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Recursos
CREATE TABLE recursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL, -- Tipo de recurso (Desarrollador, Probador, etc.)
    disponibilidad BOOLEAN DEFAULT TRUE
);

-- Tabla de Proyectos
CREATE TABLE proyectos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    descripcion TEXT,
    estado VARCHAR(50) DEFAULT 'Activo', -- Estado del proyecto (Activo, Completado, etc.)
    fecha_inicio DATETIME NOT NULL,
    fecha_fin DATETIME,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion DATETIME ON UPDATE CURRENT_TIMESTAMP
);

-- Tabla de Tareas
CREATE TABLE tareas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descripcion TEXT,
    estado VARCHAR(50) DEFAULT 'Pendiente', -- Estado de la tarea (Pendiente, En progreso, Completada)
    prioridad VARCHAR(50) NOT NULL, -- Prioridad: Baja, Media, Alta
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion DATETIME ON UPDATE CURRENT_TIMESTAMP,
    fecha_entrega DATETIME NOT NULL,
    recurso_asignado_id INT,
    proyecto_id INT,
    FOREIGN KEY (recurso_asignado_id) REFERENCES recursos(id),
    FOREIGN KEY (proyecto_id) REFERENCES proyectos(id)
);

-- Tabla de Comentarios
CREATE TABLE comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contenido TEXT NOT NULL,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario_id INT,
    tarea_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (tarea_id) REFERENCES tareas(id)
);

-- Tabla de Registro de Actividades
CREATE TABLE registro_actividades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    accion VARCHAR(200) NOT NULL,
    marca_tiempo DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Tabla de Roles de Usuario
CREATE TABLE roles_usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_rol VARCHAR(50) UNIQUE NOT NULL,
    descripcion VARCHAR(150)
);

-- Tabla para almacenar el feedback de los usuarios
CREATE TABLE feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    recomendacion VARCHAR(500) NOT NULL,
    utilidad BOOLEAN NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Insertar datos en la tabla de usuarios
INSERT INTO usuarios (nombre_usuario, correo, contrasena_hash, rol, fecha_creacion)
VALUES 
('admin', 'admin@xpertix.com', 'hashed_password', 'Administrador', NOW()),
('developer1', 'dev1@xpertix.com', 'hashed_password', 'Desarrollador', NOW()),
('tester1', 'test1@xpertix.com', 'hashed_password', 'Probador', NOW());

-- Insertar datos en la tabla de recursos
INSERT INTO recursos (nombre, tipo, disponibilidad)
VALUES 
('Desarrollador Frontend', 'Desarrollador', 1),
('Desarrollador Backend', 'Desarrollador', 1),
('Probador QA', 'Probador', 1),
('Gerente de Proyecto', 'Gerente', 1);

-- Insertar datos en la tabla de proyectos
INSERT INTO proyectos (titulo, descripcion, estado, fecha_inicio, fecha_fin, fecha_creacion)
VALUES 
('Proyecto Web Avanzado', 'Desarrollo de una aplicación web de comercio electrónico', 'Activo', '2024-01-01', '2024-06-01', NOW()),
('Aplicación Móvil E-learning', 'Desarrollo de una app de educación en línea', 'Activo', '2024-03-01', '2024-09-01', NOW());

-- Insertar datos en la tabla de tareas
INSERT INTO tareas (titulo, descripcion, estado, prioridad, fecha_creacion, fecha_entrega, recurso_asignado_id, proyecto_id)
VALUES 
('Desarrollo de Módulo de Autenticación', 'Implementar y probar el módulo de autenticación de usuarios', 'Completada', 'Alta', NOW(), '2024-02-15', 1, 1),
('Pruebas de Integración del Módulo de Pago', 'Realizar pruebas completas de integración del sistema de pagos', 'Pendiente', 'Media', NOW(), '2024-05-01', 2, 1),
('Diseño del Prototipo de Interfaz', 'Crear prototipos de baja fidelidad de la interfaz de usuario', 'En progreso', 'Media', NOW(), '2024-04-15', 3, 2);


CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL,
    PRIMARY KEY (version_num)
);


SET FOREIGN_KEY_CHECKS = 0;
SET FOREIGN_KEY_CHECKS = 1;



CREATE INDEX idx_tareas_proyecto_id ON tareas(proyecto_id);
CREATE INDEX idx_comentarios_tarea_id ON comentarios(tarea_id);

FOREIGN KEY (recurso_asignado_id) REFERENCES recursos(id) ON DELETE CASCADE,
FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) ON DELETE CASCADE

INSERT INTO usuarios (nombre_usuario, correo, contrasena_hash, rol) 
VALUES ('admin', 'admin@xpertix.com', 'hashed_password', 'Administrador');
