# 🚀 Xpertix-2.0 - Sistema Experto Extreme Programming 

Sistema Experto Para La Gestión De Tareas Basado En La Metodología Ágil Extreme Programming, con integración de reglas en Prolog y autenticación con Google.

![Logo](https://img.icons8.com/3d-fluency/94/rocket.png) <img src="./Xpertix/app/static/img/Xpertix.png">

## 🔧 Stack Tecnológico
### **Backend**
- <img src="https://img.icons8.com/color/48/python.png" width="20"/> Python 3.10+
- <img src="./Xpertix/app/static/img/image-5.png" width="20"/> Prolog
- <img src="./Xpertix/app/static/img/image-2.png" width="20"/> Flask
- <img src="./Xpertix/app/static/img/image.png" width="20"/> MariaDB

### **Frontend**
- <img src="https://img.icons8.com/color/48/html-5.png" width="20"/> HTML5
- <img src="https://img.icons8.com/color/48/css3.png" width="20"/> CSS3
- <img src="https://img.icons8.com/color/48/javascript.png" width="20"/> JavaScript
- <img src="https://img.icons8.com/color/48/bootstrap.png" width="20"/> Bootstrap 5

### **Herramientas**
- <img src="./Xpertix/app/static/img/image-6.png" width="20"/> DBeaver

## 🛠️ Instalación y Configuración

### 1. Clonar repositorio
```bash
git clone https://github.com/tu_usuario/Xpertix-2.0.git
cd Xpertix-2.0
```
### 2. Crear entorno virtual (Windows)
```bash
python -m venv venv
```
### 3. Activar entorno virtual
```bash
venv\Scripts\activate
```
### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```
## ⚙️ Configuración Esencial
### 🔐 Autenticación con Google
1. Crea un proyecto en Google Cloud Console: https://console.cloud.google.com/
2. Ve a *APIs y Servicios* > *Credenciales*
3. Configura OAuth con:
- Tipo de aplicación: Web
- URI de redireccionamiento: http://localhost:5000/google_login/callback

4. Actualiza en rutas.py:
```bash
google_bp = make_google_blueprint(
    client_id='TU_CLIENT_ID',
    client_secret='TU_CLIENT_SECRET',
    # ... resto de configuración
)
```
5. Descargar el archivo .json que contiene el client_secret y pegarlo en la raiz del proyecto
6. Configurar en config.py:
```bash
import os
class Configuracion:
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave_secreta_super_segura')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://usuario:contraseña@localhost/nombre_bd')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### 🗄️ Configurar MariaDB
1. Instalar MariaDB
- Preferiblemente DBeaver para gestionar MariaDB
2. Crear base de datos:
```bash
CREATE DATABASE xpertix_db;
CREATE USER 'xpertix_user'@'localhost' IDENTIFIED BY 'tu_password';
GRANT ALL PRIVILEGES ON xpertix_db.* TO 'xpertix_user'@'localhost';
FLUSH PRIVILEGES;
```
## ▶️ Ejecutar el Sistema
```bash
flask db init
flask db migrate
flask db upgrade
python run.py
```
Accede desde: http://localhost:5000

## 🕹️ Funcionalidades Clave
-  **🔑 Autenticación con Google** - Registro/Login en 1 clic

- **📂 Gestión de Proyectos** - Creación y seguimiento con sprints automáticos

- **📊 Panel de Control** - Seguimiento en tiempo real

- **🔄 Motor de Reglas Expertas** - Toma decisiones basadas en Prolog

- **🔔 Notificaciones Inteligentes** - Alertas de progreso

##  🚨 Solución de Problemas Comunes

| Problema                       | Solución                                                                 |
|--------------------------------|--------------------------------------------------------------------------|
| `Error 1045: Access denied`    | Verificar usuario/contraseña en `SQLALCHEMY_DATABASE_URI`               |
| `SQLAlchemy OperationalError`  | Asegurar que MariaDB está corriendo:<br>`sudo systemctl start mariadb`  |
| `ModuleNotFoundError: pymysql` | Ejecutar:<br>`pip install pymysql`                                      |
| `Relation does not exist`      | Ejecutar:<br>`flask db upgrade`                                         |

## 📂 Estructura del Proyecto
```bash
Xpertix-2.0/
├ app/                  # Carpeta de proyecto principal
├── static/             # CSS/JS/IMG
├── templates/          # Vistas HTML
├ extensiones.py        # Configurar a BD
├ formularios.py        # Vistas HTML
├ modelos.py            # Modelos de base de datos
├ rutas.py              # Llamada de rutas
├ script.sql            # Script de BD
├ utilidades.py         # Reglas interactuar en vivo
├ inference/            # Carpeta de prolog configuración
├ conector_api.py       # Configurar interacciones con Sistema y Prolog
├ motor.pl              # Reglas predefinidas Prolog
├ .env                  # Archivo configuración BD
├ config.py             # Migraciones de BD
├ requirements.txt      # Dependencias
├ run.py                # Archivo para ejecutar sistema
└── README.md           # Este archivo
```
## 🔄 Actualizar Base de Datos
```bash
flask db migrate -m "Descripción de cambios"
flask db upgrade
```
