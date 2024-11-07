from .modelos import Tarea, Recurso

def obtener_recursos_disponibles():
    """Devuelve todos los recursos disponibles de la base de datos."""
    return Recurso.query.filter_by(disponibilidad=True).all()

def marcar_tarea_completada(id_tarea):
    """Marca una tarea como completada y actualiza la disponibilidad del recurso asignado."""
    tarea = Tarea.query.get(id_tarea)
    if tarea:
        tarea.estado = 'Completada'
        tarea.recurso_asignado.disponibilidad = True
        db.session.commit()
        return True
    return False

def reasignar_tarea(id_tarea, id_nuevo_recurso):
    """Reasigna una tarea a un nuevo recurso."""
    tarea = Tarea.query.get(id_tarea)
    nuevo_recurso = Recurso.query.get(id_nuevo_recurso)
    if tarea and nuevo_recurso:
        tarea.recurso_asignado_id = id_nuevo_recurso
        db.session.commit()
        return True
    return False
