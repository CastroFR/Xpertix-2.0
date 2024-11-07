import os
class Configuracion:
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave_secreta_super_segura')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://root:1234@localhost/xpertix_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
