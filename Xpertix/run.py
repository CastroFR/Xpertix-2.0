from app.__init__ import app
#import sys
#import os

#sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# from app import crear_app

# app = crear_app()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

from app.db import db

db.init_app(app)
#app = crear_app()
with app.app_context():  # Asegura que todo lo que sigue ocurra dentro del contexto de la app
    db.create_all()  # Opcional: crear tablas si no existen

if __name__ == '__main__':
   
    app.run(host='0.0.0.0', port=5000, debug=True)
