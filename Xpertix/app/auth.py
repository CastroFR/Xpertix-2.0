# from flask import Blueprint, render_template, redirect, url_for, flash, request
# from flask_login import login_user, logout_user
# from werkzeug.security import check_password_hash
# from app.modelos import db, Usuario

# auth_blueprint = Blueprint('auth', __name__)

# @auth_blueprint.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         nombre_usuario = request.form.get('nombre_usuario')
#         contrasena = request.form.get('contrasena')
        
#         usuario = Usuario.query.filter_by(nombre_usuario=nombre_usuario).first()

#         if usuario and check_password_hash(usuario.contrasena_hash, contrasena):
#             login_user(usuario)
#             flash('Inicio de sesión exitoso', 'success')
#             return redirect(url_for('principal.index'))
#         else:
#             flash('Usuario o contraseña incorrectos', 'danger')
    
#     return render_template('auth/login.html')

# @auth_blueprint.route('/logout')
# def logout():
#     logout_user()
#     flash('Has cerrado sesión correctamente', 'info')
#     return redirect(url_for('auth.login'))
