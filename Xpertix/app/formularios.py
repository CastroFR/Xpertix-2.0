from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField, SubmitField, DateField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class FormularioRecurso(FlaskForm):
    nombre = StringField('Nombre del Recurso', validators=[DataRequired(), Length(max=100)])
    tipo = SelectField('Tipo', choices=[('Desarrollador', 'Desarrollador'), ('Probador', 'Probador'), ('Gerente', 'Gerente')], validators=[DataRequired()])
    disponibilidad = BooleanField('Disponible')
    enviar = SubmitField('Agregar Recurso')

class FormularioTarea(FlaskForm):
    titulo = StringField('Título de la Tarea', validators=[DataRequired(), Length(max=150)])
    descripcion = TextAreaField('Descripción', validators=[Length(max=500)])
    recurso_asignado_id = SelectField('Asignar Recurso', coerce=int)
    proyecto_id = SelectField('Asignar Proyecto', coerce=int)
    prioridad = SelectField('Prioridad', choices=[('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta')], validators=[DataRequired()])
    fecha_entrega = DateField('Fecha de Entrega', format='%Y-%m-%d', validators=[DataRequired()])
    enviar = SubmitField('Crear Tarea')

class FormularioProyecto(FlaskForm):
    titulo = StringField('Título del Proyecto', validators=[DataRequired(), Length(max=200)])
    descripcion = TextAreaField('Descripción', validators=[Length(max=500)])
    fecha_inicio = DateField('Fecha de Inicio', format='%Y-%m-%d', validators=[DataRequired()])
    fecha_fin = DateField('Fecha de Fin (Opcional)', format='%Y-%m-%d', validators=[])
    enviar = SubmitField('Agregar Proyecto')