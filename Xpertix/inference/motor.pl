:- discontiguous recomendacion_asignacion/2.
:- discontiguous prioridad_alta/2.
:- discontiguous prioridad_media/2.
:- discontiguous recurso_optimo/2.


% Definición de recursos y sus habilidades
recurso(disponible, 'Desarrollador', ['Python', 'React']).
recurso(disponible, 'Probador', ['Selenium', 'JUnit']).
recurso(disponible, 'Gerente de Proyecto', ['Scrum', 'Kanban']).

% Reglas de recomendación de asignación de recursos a tareas
recomendacion_asignacion('Desarrollo de Módulo de Autenticación', 'Desarrollador').
recomendacion_asignacion('Pruebas de Integración del Módulo de Pago', 'Probador').
recomendacion_asignacion('Planificación del sprint', 'Gerente de Proyecto').

% Regla para recomendar la asignación de recursos a tareas basadas en habilidades
recomendacion_asignacion(Tarea, Recurso) :-
    recurso(disponible, Recurso, Habilidades),
    tarea_necesaria(Tarea, HabilidadesRequeridas),
    subset(HabilidadesRequeridas, Habilidades),
    format('Recomendación: asignar el recurso ~w a la tarea ~w', [Recurso, Tarea]).

% Ejemplo de tareas necesarias y habilidades requeridas
tarea_necesaria('Desarrollo de módulo de autenticación', ['Python']).
tarea_necesaria('Pruebas de integración', ['Selenium']).
tarea_necesaria('Desarrollo frontend', ['React']).
tarea_necesaria('Planificación del sprint', ['Scrum']).

% Función para verificar si una lista es subconjunto de otra
subset([], _).
subset([H|T], L) :-
    member(H, L),
    subset(T, L).

% Reglas para gestión de cambios en el proyecto
ajuste_asignacion(Tarea, RecursoAnterior, RecursoNuevo) :-
    recurso(disponible, RecursoNuevo),
    \+ RecursoNuevo = RecursoAnterior,
    format('Asignación ajustada: cambiar de ~w a ~w para la tarea ~w', [RecursoAnterior, RecursoNuevo, Tarea]).



% Ejemplos de reglas en Prolog para proyectos y recomendaciones
recurso_optimo(proyecto_web, desarrollador_frontend).
recurso_optimo(proyecto_movil, desarrollador_android).
recurso_optimo(proyecto_movil, probador).

tarea_comun(proyecto_web, "Crear página de inicio").
tarea_comun(proyecto_movil, "Desarrollar módulo de autenticación").

prioridad_alta(tarea, "Desarrollar sistema de pago").
prioridad_media(tarea, "Diseñar prototipo de interfaz").

% Recursos adicionales
recurso(disponible, 'Desarrollador Frontend').
recurso(disponible, 'Desarrollador Backend').
recurso(disponible, 'Probador QA').
recurso(disponible, 'Gerente de Proyecto').

% Tareas adicionales
tarea_necesaria('Desarrollo de Módulo de Autenticación').
tarea_necesaria('Pruebas de Integración del Módulo de Pago').
tarea_necesaria('Diseño del Prototipo de Interfaz').
tarea_necesaria('Planificación de Sprint').
tarea_necesaria('Revisión de Código').

% Reglas de recomendación extendida
recomendacion_asignacion('Desarrollo de Módulo de Autenticación', 'Desarrollador Backend').
recomendacion_asignacion('Pruebas de Integración del Módulo de Pago', 'Probador QA').
recomendacion_asignacion('Diseño del Prototipo de Interfaz', 'Desarrollador Frontend').

% Prioridades
prioridad_alta(tarea, 'Desarrollo de Módulo de Autenticación').
prioridad_media(tarea, 'Diseño del Prototipo de Interfaz').
prioridad_baja(tarea, 'Revisión de Documentación').

% Proyecto y recursos óptimos
recurso_optimo(proyecto_web, 'Desarrollador Frontend').
recurso_optimo(proyecto_web, 'Probador QA').
recurso_optimo(proyecto_movil, 'Desarrollador Backend').
recurso_optimo(proyecto_movil, 'Probador').

