Guía de Instalación y Manejo del Sistema Experto desde GitHub

1. Requisitos Previos
Antes de comenzar, asegúrate de tener instaladas las siguientes herramientas y configuraciones:

Sistema Operativo Compatible:

Windows, macOS o Linux.
Software Requerido:

Python 3.9 o superior.
Git (para clonar el repositorio).
MariaDB (para la base de datos).
Un entorno virtual (opcional, pero recomendado).
Librerías de Python:

Flask.
Flask-SQLAlchemy.
Flask-Login.
PyMySQL.

2. Descarga del Código desde GitHub
Clonar el Repositorio:

Abre tu terminal o línea de comandos.
Navega al directorio donde deseas descargar el proyecto.

git clone https://github.com/tu_usuario/sistema-experto.git
Reemplaza https://github.com/tu_usuario/sistema-experto.git con la URL de tu repositorio.
Acceder al Proyecto:

Navega al directorio del proyecto 

3. Configuración del Entorno Virtual (Opcional)
Crear el Entorno Virtual:

En tu terminal, ejecuta:

python -m venv venv
Activar el Entorno Virtual:

En Windows:

.\venv\Scripts\activate
En macOS/Linux:

source venv/bin/activate
Instalar las Dependencias:

Ejecuta el comando:

pip install -r requirements.txt

4. Configuración de la Base de Datos
Configurar MariaDB:

Asegúrate de que MariaDB esté instalado y ejecutándose.
Abre el cliente de MariaDB:

mysql -u root -p
Crea la base de datos para el sistema:

CREATE DATABASE sistema_experto;
Configurar las Credenciales:

Abre el archivo config.py en el directorio del proyecto.
Actualiza las credenciales de la base de datos:


SQLALCHEMY_DATABASE_URI = "mysql+pymysql://usuario:contraseña@localhost/sistema_experto"
Reemplaza usuario y contraseña con tus credenciales de MariaDB.

Inicializar la Base de Datos:

En tu terminal, ejecuta:

flask db init
flask db migrate -m "Creación inicial de tablas"
flask db upgrade

5. Ejecución del Sistema
Iniciar el Servidor:

En la terminal, ejecuta:

flask run
Esto iniciará el servidor en la dirección predeterminada: http://127.0.0.1:5000.

Acceder al Sistema:

Abre un navegador web y ve a la dirección http://127.0.0.1:5000.

6. Administración del Sistema
Primer Usuario Administrador:

Accede al sistema con el primer usuario administrador que debes crear desde la base de datos o con una ruta predefinida.
Ejemplo de creación manual desde MariaDB:

INSERT INTO usuarios (nombre_usuario, correo, contrasena_hash, rol)
VALUES ('admin', 'admin@example.com', 'hashed_password', 'Administrador');
Gestión de Proyectos y Tareas:

Crea proyectos desde la interfaz en la sección Proyectos.
Genera automáticamente sprints y tareas a partir de los requisitos.
Seguimiento y Reportes:

Consulta el progreso de cada proyecto en tiempo real desde los paneles de visualización.
Descarga reportes en formato PDF o Excel desde la sección Reportes.

7. Resolución de Problemas Comunes
Problema	Solución
Error de conexión a la base de datos	Verifica que MariaDB esté ejecutándose y que las credenciales en config.py sean correctas.
Librerías faltantes	Asegúrate de haber ejecutado pip install -r requirements.txt en el entorno virtual.
Fallos en el servidor Flask	Revisa los logs en la terminal para identificar errores específicos.

8. Actualización del Sistema
Actualizar el Código desde GitHub:

En el directorio del proyecto, ejecuta:

git pull origin main
Actualizar la Base de Datos (si es necesario):

Ejecuta las migraciones:

flask db migrate -m "Actualización"
flask db upgrade

9. Contacto para Soporte
Si tienes problemas durante la instalación o uso, puedes abrir un ticket en el repositorio de GitHub o escribir a: soporte@sistemaexperto.com.











Manual de Usuario del Sistema Experto para Gestión de Proyectos

1. Introducción
Este manual tiene como objetivo guiar al usuario final en el uso del sistema experto para la gestión de proyectos. El sistema permite automatizar la planificación, asignación de recursos y seguimiento de tareas, haciendo uso de reglas predefinidas en la base de conocimientos.

2. Acceso al Sistema
Iniciar Sesión:

Abra el sistema desde su navegador ingresando la dirección proporcionada.
Ingrese su correo electrónico y contraseña en el formulario de inicio de sesión.
Haga clic en el botón Iniciar Sesión.
Recuperar Contraseña (si aplica):

Si olvidó su contraseña, haga clic en el enlace Recuperar Contraseña.
Siga las instrucciones para recibir un correo de recuperación.

3. Registro de Usuarios
Acceda a la sección Usuarios desde el panel principal.
Haga clic en el botón Registrar Nuevo Usuario.
Complete los campos requeridos:
Nombre de usuario.
Correo electrónico.
Contraseña.
Seleccione el rol del usuario (Desarrollador, Probador, Gerente, etc.).
Haga clic en Guardar para registrar el usuario.

4. Creación de Proyectos
Acceda a la sección Proyectos desde el menú principal.
Haga clic en el botón Crear Proyecto.
Complete el formulario:
Título del proyecto: Nombre del proyecto.
Descripción: Detalles generales del proyecto.
Fecha de inicio y Fecha de fin.
Requisitos: Describa los requerimientos clave del proyecto.
Haga clic en Guardar para registrar el proyecto.

5. Generación Automática de Sprints y Tareas
Seleccione un proyecto desde la lista en la sección Proyectos.
Haga clic en el botón Generar Sprints.
El sistema analizará los requisitos y generará automáticamente:
Sprints: Divisiones del proyecto en fases.
Tareas: Acciones específicas dentro de cada sprint.
Revise las tareas generadas en el panel del proyecto.

6. Asignación de Recursos
Vaya a la sección Recursos.
Seleccione un recurso disponible (desarrollador, probador, etc.).
Haga clic en el botón Asignar Tarea.
Elija la tarea y confirme la asignación.

7. Seguimiento del Progreso
Acceda al panel del proyecto desde la sección Proyectos.
Visualice el estado actual de los sprints y tareas mediante gráficos y tablas.
Marque tareas como completadas haciendo clic en el botón Completar junto a la tarea.

8. Gestión de Comentarios
En la vista de detalles del proyecto, seleccione una tarea.
Agregue un comentario en el campo correspondiente y haga clic en Enviar Comentario.
Los comentarios serán visibles para todos los usuarios asignados al proyecto.

9. Generación de Reportes
Acceda a la sección Reportes.
Seleccione un proyecto y el tipo de reporte que desea generar (Progreso, Tareas, Recursos).
Descargue el reporte en formato PDF o Excel.

10. Notificaciones
Revise las notificaciones en el ícono de la campana en la esquina superior derecha.
Las notificaciones incluyen:
Tareas próximas a vencer.
Cambios realizados en el proyecto.
Actividades completadas por otros usuarios.

11. Cierre de Sesión
Haga clic en su perfil (ícono en la esquina superior derecha).
Seleccione la opción Cerrar Sesión.

12. Solución de Problemas Comunes
Problema	Solución
No puedo iniciar sesión	Verifique su correo y contraseña. Use la opción de recuperación si es necesario.
Tareas no se generan automáticamente	Asegúrese de haber ingresado requisitos claros en el proyecto.
No puedo asignar recursos	Confirme que el recurso esté disponible y registrado en el sistema.

13. Contacto de Soporte
Si encuentra problemas adicionales, comuníquese con el soporte técnico enviando un correo a: soporte@sistemaexperto.com.

Nota: Este sistema se actualiza periódicamente. Consulte las actualizaciones disponibles en la sección de Ayuda.