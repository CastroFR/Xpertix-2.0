from app.db import db

from flask import Blueprint, current_app, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.modelos import Proyecto, Usuario, Recurso, Tarea, Comentario, RegistroActividad, Feedback

from .formularios import FormularioRecurso, FormularioTarea, FormularioProyecto
from inference.conector_api import obtener_recomendacion, optimizar_carga_trabajo, ajustar_asignacion 
from functools import wraps
#from flask import current_app



principal = Blueprint('principal', __name__)

@principal.route('/')
def inicio():
    
    
    proyectos = Proyecto.query.all()  # Realiza la consulta
    return render_template('index.html', proyectos=proyectos)
        
        

@principal.route('/proyecto/<int:id>')
def ver_detalles_proyecto(id):
    proyecto = Proyecto.query.get_or_404(id)
    tareas = Tarea.query.filter_by(proyecto_id=id).all()
    return render_template('detalles_proyecto.html', proyecto=proyecto, tareas=tareas)

def registrar_principal(app):
    app.register_blueprint(principal)

#--- Ruta para crear/agregar nuevos proyectos

@principal.route('/agregar_proyecto', methods=['GET', 'POST'])
def agregar_proyecto():
    formulario = FormularioProyecto()
    if formulario.validate_on_submit():
        nuevo_proyecto = Proyecto(
            titulo=formulario.titulo.data,
            descripcion=formulario.descripcion.data,
            fecha_inicio=formulario.fecha_inicio.data,
            fecha_fin=formulario.fecha_fin.data
        )
        db.session.add(nuevo_proyecto)
        db.session.commit()
        
        # Registrar la actividad después de definir nuevo_proyecto
        #registrar_actividad(1, f'Proyecto "{nuevo_proyecto.titulo}" agregado')
        
        flash('¡Proyecto agregado exitosamente!', 'success')
        return redirect(url_for('principal.inicio'))
    return render_template('agregar_proyecto.html', formulario=formulario)
#----

#-----
# Rutas para Editar y Eliminar proyectos
@principal.route('/editar_proyecto/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_proyecto(id):
    proyecto = Proyecto.query.get_or_404(id)
    if request.method == 'POST':
        proyecto.titulo = request.form['titulo']
        proyecto.descripcion = request.form['descripcion']
        proyecto.estado = request.form['estado']
        db.session.commit()
        flash('¡Proyecto actualizado exitosamente!', 'success')
        return redirect(url_for('principal.inicio'))
    return render_template('editar_proyecto.html', proyecto=proyecto)

@principal.route('/eliminar_proyecto/<int:id>', methods=['POST'])
def eliminar_proyecto(id):
    proyecto = Proyecto.query.get_or_404(id)
    db.session.delete(proyecto)
    db.session.commit()
    flash('¡Proyecto eliminado exitosamente!', 'success')
    return redirect(url_for('principal.inicio'))

#-----
@principal.route('/agregar_recurso', methods=['GET', 'POST'])
def agregar_recurso():
    formulario = FormularioRecurso()
    if formulario.validate_on_submit():
        nuevo_recurso = Recurso(
            nombre=formulario.nombre.data,
            tipo=formulario.tipo.data,
            disponibilidad=formulario.disponibilidad.data
        )
        db.session.add(nuevo_recurso)
        db.session.commit()
        flash('¡Recurso agregado exitosamente!', 'success')
        return redirect(url_for('principal.inicio'))
    return render_template('agregar_recurso.html', formulario=formulario)

@principal.route('/recursos')
def listar_recursos():
    recursos = Recurso.query.all()
    return render_template('listar_recursos.html', recursos=recursos)

@principal.route('/agregar_tarea', methods=['GET', 'POST'])
def agregar_tarea():
    formulario = FormularioTarea()
    formulario.recurso_asignado_id.choices = [(r.id, r.nombre) for r in Recurso.query.filter_by(disponibilidad=True).all()]
    formulario.proyecto_id.choices = [(p.id, p.titulo) for p in Proyecto.query.all()]

    if formulario.validate_on_submit():
        nueva_tarea = Tarea(
            titulo=formulario.titulo.data,
            descripcion=formulario.descripcion.data,
            recurso_asignado_id=formulario.recurso_asignado_id.data,
            proyecto_id=formulario.proyecto_id.data,
            prioridad=formulario.prioridad.data,
            fecha_entrega=formulario.fecha_entrega.data
        )
        db.session.add(nueva_tarea)
        db.session.commit()

        # Registrar la actividad
#        nueva_actividad = RegistroActividad(
#            accion=f'Tarea "{nueva_tarea.titulo}" creada',
#            usuario_id=1  # Reemplazar por el usuario autenticado cuando se integre el Login
#        )
#        db.session.add(nueva_actividad)
#        db.session.commit()

#        flash('¡Tarea agregada exitosamente!', 'success')
#        return redirect(url_for('principal.inicio'))


        # Verificar que el usuario existe antes de registrar la actividad
        usuario_id = 1  # Puedes cambiar esto a session.get('usuario_id') si estás usando autenticación
        usuario = Usuario.query.get(usuario_id)
        if usuario:
            nueva_actividad = RegistroActividad(
                accion=f'Tarea "{nueva_tarea.titulo}" creada',
                usuario_id=usuario_id
            )
            db.session.add(nueva_actividad)
            db.session.commit()
        else:
            flash('Error: No se encontró el usuario para registrar la actividad.', 'danger')

        flash('¡Tarea agregada exitosamente!', 'success')
        return redirect(url_for('principal.inicio'))
    return render_template('agregar_tarea.html', formulario=formulario)

@principal.route('/tareas')
def lista_tareas():
    tareas = Tarea.query.all()
    return render_template('lista_tareas.html', tareas=tareas)

#-----
#Ruta para marcar Tareas como completadas

@principal.route('/completar_tarea/<int:id>', methods=['POST'])
def completar_tarea(id):
    tarea = Tarea.query.get_or_404(id)
    tarea.estado = 'Completada'
    if tarea.recurso_asignado:
        tarea.recurso_asignado.disponibilidad = True  # Liberar el recurso asignado al completar la tarea
    db.session.commit()
    
    # Registrar la actividad
    nueva_actividad = RegistroActividad(
        accion=f'Tarea "{tarea.titulo}" marcada como completada',
        usuario_id=1  # Reemplazar por el usuario autenticado cuando se integre el Login
    )
    db.session.add(nueva_actividad)
    db.session.commit()

    flash('¡Tarea marcada como completada!', 'success')
    return redirect(url_for('principal.detalles_proyecto', id=tarea.proyecto_id))
#-----

@principal.route('/detalles_proyecto/<int:id>')
def detalles_proyecto(id):
    proyecto = Proyecto.query.get_or_404(id)
    return render_template('detalles_proyecto.html', proyecto=proyecto)

@principal.route('/comentarios/<int:tarea_id>', methods=['GET', 'POST'])
def comentarios(tarea_id):
    tarea = Tarea.query.get_or_404(tarea_id)
    if request.method == 'POST':
        contenido = request.form['contenido']
        nuevo_comentario = Comentario(contenido=contenido, usuario_id=1, tarea_id=tarea_id)  # Cambiar el usuario_id según el usuario autenticado
        db.session.add(nuevo_comentario)
        db.session.commit()

        # Registrar la actividad
        nueva_actividad = RegistroActividad(
            accion=f'Comentario agregado a la tarea "{tarea.titulo}"',
            usuario_id=1 # Reemplazar con el usuario autenticado
        )
        db.session.add(nuevo_comentario)
        db.session.commit()        

        flash('¡Comentario agregado!', 'success')
        return redirect(url_for('principal.comentarios', tarea_id=tarea_id))
    comentarios = Comentario.query.filter_by(tarea_id=tarea_id).all()
    return render_template('comentarios.html', tarea=tarea, comentarios=comentarios)

#Rutas para poder crear, editar y eliminar usuarios

@principal.route('/usuarios')
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('listar_usuarios.html', usuarios=usuarios)

@principal.route('/actualizar_usuario/<int:usuario_id>', methods=['GET', 'POST'])
def actualizar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        usuario.nombre_usuario = request.form['nombre_usuario']
        usuario.rol = request.form['rol']
        db.session.commit()
        flash('¡Usuario actualizado exitosamente!', 'success')
        return redirect(url_for('principal.listar_usuarios'))
    return render_template('editar_usuario.html', usuario=usuario)


@principal.route('/eliminar_usuario/<int:id>', methods=['POST'])
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('¡Usuario eliminado exitosamente!', 'success')
    return redirect(url_for('principal.listar_usuarios'))

#--------

#Ruta para mostrar el Historial

@principal.route('/registro_actividades', methods=['GET'])
def registro_actividades():
    # Consultar las actividades registradas
    actividades = RegistroActividad.query.order_by(RegistroActividad.marca_tiempo.desc()).all()

    # Renderizar una página para mostrar las actividades
    return render_template('registro_actividades.html', actividades=actividades)

       
        #return redirect(url_for('principal.inicio'))

# Ejemplo de uso:
#registrar_actividad(1, f'Proyecto "{nuevo_proyecto.titulo}" agregado')

# Ruta para Notificaciones

@principal.route('/notificaciones', methods=['GET'])
def notificaciones():
    # Ejemplo simple: mostrar las últimas actividades registradas como notificaciones
    actividades = RegistroActividad.query.order_by(RegistroActividad.marca_tiempo.desc()).limit(10).all()
    return render_template('notificaciones.html', actividades=actividades)

# Ruta para Recomendaciones, basadas en proyectos pasados
# y reglas del sistema.

@principal.route('/recomendaciones/<int:proyecto_id>', methods=['GET'])
def recomendaciones(proyecto_id):
    proyecto = Proyecto.query.get_or_404(proyecto_id)
    recomendaciones = obtener_recomendaciones(proyecto)
    print("Recomendaciones generadas:", recomendaciones)
    if not recomendaciones:
        print("No se generaron recomendaciones")
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template('recomendaciones_fragmento.html', recomendaciones=recomendaciones)
    return render_template('recomendaciones.html', proyecto=proyecto, recomendaciones=recomendaciones)

def obtener_recomendaciones(proyecto):
    recomendaciones = []
    # Agrega una verificación para depurar
    print(f"Proyecto recibido: {proyecto.titulo}")

    # Recomendaciones basadas en Prolog
    for tarea in proyecto.tareas:
        recomendacion = obtener_recomendacion(tarea.titulo)
        if recomendacion:
            recomendaciones.append(f"Recomendación para '{tarea.titulo}': {', '.join(recomendacion)}")
        else:
            recomendaciones.append(f"No se encontraron recomendaciones específicas para '{tarea.titulo}'")

    return recomendaciones

    # Sugerencias adicionales basadas en lógica de la base de datos (como ya tienes)
    tareas_similares = Tarea.query.filter(Tarea.proyecto_id != proyecto.id).all()
    for tarea in tareas_similares:
        if tarea.prioridad == 'Alta' and tarea.estado == 'Completada':
            recomendaciones.append(f"Considera agregar una tarea similar a '{tarea.titulo}' con alta prioridad.")
    
    recursos_disponibles = Recurso.query.filter_by(disponibilidad=True).all()
    if recursos_disponibles:
        recomendaciones.append(f"Recomendación: Asigna el recurso '{recursos_disponibles[0].nombre}' para una tarea importante.")
    
    if 'web' in proyecto.titulo.lower():
        recomendaciones.append("Considera usar frameworks como React o Vue.js para desarrollo web.")
    
    return recomendaciones

# Ruta para enviar Feedback

@principal.route('/enviar_feedback', methods=['POST'])
def enviar_feedback():
    usuario_id = 1  # Cambiar por el ID del usuario autenticado cuando se integre el Login
    recomendacion = request.form['recomendacion']
    utilidad = request.form['utilidad'] == 'true'

    nuevo_feedback = Feedback(
        usuario_id=usuario_id,
        recomendacion=recomendacion,
        utilidad=utilidad
    )
    db.session.add(nuevo_feedback)
    db.session.commit()

    flash('¡Gracias por tu feedback!', 'success')
    return redirect(request.referrer or url_for('principal.inicio'))


@principal.route('/editar_usuario/<int:usuario_id>', methods=['GET', 'POST'])
def editar_usuario(usuario_id):
    usuario = Usuario.query.get_or_404(usuario_id)
    return render_template('editar_usuario.html', usuario=usuario)


@principal.route('/usuarios/nuevo', methods=['GET', 'POST'])
def nuevo_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        rol = request.form['rol']  # Obtener el rol del formulario

        nuevo_usuario = Usuario(nombre=nombre, email=email, rol=rol)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash("Usuario creado exitosamente.", "success")
        return redirect(url_for('principal.listar_usuarios'))

    return render_template('formulario_usuario.html')


@principal.route('/test')
def test():
    return "La aplicación está funcionando correctamente"



""" def rol_requerido(rol):
    def decorator(f):
        @wraps(f)
        def wrapped_function(*args, **kwargs):
            if current_user.rol != rol:
                abort(403)
            return f(*args, **kwargs)
        return wrapped_function
    return decorator

@principal.route('/establecer_prioridades')
@rol_requerido('Customer')
def establecer_prioridades():
    # Lógica para el cliente (Customer)
    pass


def roles_requeridos(*roles):
    def decorator(f):
        @wraps(f)
        def wrapped_function(*args, **kwargs):
            if current_user.rol not in roles:
                abort(403)
            return f(*args, **kwargs)
        return wrapped_function
    return decorator

# Ejemplo de uso
@principal.route('/monitorear_progreso')
@roles_requeridos('Tracker', 'Coach')
def monitorear_progreso():
    # Lógica para los roles de Tracker y Coach
    pass
 """
