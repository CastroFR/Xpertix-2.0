from app.db import db
from datetime import datetime

#Tabla de Proyectos
class Proyecto(db.Model):
    __tablename__ = 'proyectos'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    estado = db.Column(db.String(50), default='Activo')  # Estado del proyecto (Activo, Completado, etc.)
    fecha_inicio = db.Column(db.DateTime, nullable=False)
    fecha_fin = db.Column(db.DateTime, nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
    tareas = db.relationship('Tarea', backref='proyecto', cascade='all, delete', lazy='dynamic')


    def __repr__(self):
        return f'<Proyecto {self.titulo}>'


# Tabla de Usuarios
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(100), unique=True, nullable=False)
    correo = db.Column(db.String(150), unique=True, nullable=False)
    contrasena_hash = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(50), nullable=False)  # Roles: Desarrollador, Probador, Gerente, etc.
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (db.Index('idx_nombre_usuario', 'nombre_usuario'),)


    def __repr__(self):
        return f'<Usuario {self.nombre_usuario}>'

# Tabla de Recursos
class Recurso(db.Model):
    __tablename__ = 'recursos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # Tipo de recurso (desarrollador, probador, etc.)
    disponibilidad = db.Column(db.Boolean, default=True)
    tareas_asignadas = db.relationship('Tarea', backref='recurso_asignado', lazy=True)

    def __repr__(self):
        return f'<Recurso {self.nombre}>'


# Tabla de Tareas
class Tarea(db.Model):
    __tablename__ = 'tareas'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    estado = db.Column(db.String(50), default='Pendiente')  # Estado de la tarea (Pendiente, En progreso, Completada)
    prioridad = db.Column(db.String(50), nullable=False)  # Prioridad: Baja, Media, Alta
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.DateTime, onupdate=datetime.utcnow)
    fecha_entrega = db.Column(db.DateTime, nullable=False)

    recurso_asignado_id = db.Column(db.Integer, db.ForeignKey('recursos.id', ondelete="CASCADE"))
    proyecto_id = db.Column(db.Integer, db.ForeignKey('proyectos.id', ondelete="CASCADE"))

    def __repr__(self):
        return f'<Tarea {self.titulo}>'

# Tabla de Comentarios
class Comentario(db.Model):
    __tablename__ = 'comentarios'
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    tarea_id = db.Column(db.Integer, db.ForeignKey('tareas.id'))

    usuario = db.relationship('Usuario', backref='comentarios', lazy=True)
    tarea = db.relationship('Tarea', backref='comentarios', lazy=True)

    def __repr__(self):
        return f'<Comentario {self.id} por Usuario {self.usuario_id}>'

# Tabla de Registro de Actividades
class RegistroActividad(db.Model):
    __tablename__ = 'registro_actividades'
    id = db.Column(db.Integer, primary_key=True)
    accion = db.Column(db.String(200), nullable=False)
    marca_tiempo = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    usuario = db.relationship('Usuario', backref='registro_actividades', lazy=True)

    def __repr__(self):
        return f'<RegistroActividad {self.accion} por Usuario {self.usuario_id}>'

# Tabla de Roles de Usuario (Opcional para roles extendidos)
class RolUsuario(db.Model):
    __tablename__ = 'roles_usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.String(50), unique=True, nullable=False)
    descripcion = db.Column(db.String(150), nullable=True)

    def __repr__(self):
        return f'<RolUsuario {self.nombre_rol}>'

# Tabla de Feedback de usuario sobre recomendaciones
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    recomendacion = db.Column(db.String(500), nullable=False)
    utilidad = db.Column(db.Boolean, nullable=False)

    usuario = db.relationship('Usuario', backref='feedbacks', lazy=True)

    def __repr__(self):
        return f'<Feedback de Usuario {self.usuario_id} sobre Recomendación>'
