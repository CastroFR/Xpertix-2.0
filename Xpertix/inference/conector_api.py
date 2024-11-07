import os
from pathlib import Path
from pyswip import Prolog

def obtener_recomendacion(tarea):
    try:
        prolog = Prolog()
        ruta_archivo = Path(__file__).parent / "motor.pl"
        prolog.consult(ruta_archivo.as_posix())
        resultado = list(prolog.query(f"recomendacion_asignacion('{tarea}', Recurso)", maxresult=1))
        return [r['Recurso'] for r in resultado] if resultado else []
    except Exception as e:
        print(f"Error en la consulta a Prolog: {e}")
        return []


def optimizar_carga_trabajo(tarea):
    try:
        prolog = Prolog()
        prolog.consult(Path(__file__).parent / "motor.pl")
        return list(prolog.query(f"optimizar_carga(Recurso, '{tarea}')"))
    except Exception as e:
        print(f"Error en la optimización de carga: {e}")
        return []

def ajustar_asignacion(tarea, recurso_anterior, recurso_nuevo):
    """Ajusta la asignación de recursos en función de la disponibilidad."""
    prolog = Prolog()
    prolog.consult("inference/motor.pl")
    resultado = list(prolog.query(f"ajuste_asignacion('{tarea}', '{recurso_anterior}', '{recurso_nuevo}')"))
    return len(resultado) > 0

