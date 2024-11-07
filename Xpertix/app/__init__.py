from flask import Flask

# #def crear_app():
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/xpertix_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'clave_secreta'

#Inicializa SQLAlchemy con la aplicación
#db.init_app(app)

    # Importa y registra blueprints
from app.rutas import principal
app.register_blueprint(principal)

#return app  
