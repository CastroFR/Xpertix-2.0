function confirmarEliminacion(mensaje) {
    return confirm(mensaje || "¿Estás seguro de que deseas realizar esta acción?");
}


document.addEventListener('DOMContentLoaded', function() {
     // Código JavaScript para manejar interacciones específicas
    console.log("Página cargada correctamente.");

    // Confirmación antes de acciones críticas
    document.querySelectorAll('.confirmar-eliminacion').forEach(function(elemento) {
        elemento.addEventListener('click', function() {
            return confirmarEliminacion("¿Estás seguro de que deseas eliminar este elemento?");
        });
    });

    // Animación de carga para botones
    document.querySelectorAll('.boton').forEach(function(boton) {
        boton.addEventListener('click', function() {
            boton.textContent = 'Procesando...';
            boton.disabled = true;
            setTimeout(() => {
                boton.textContent = 'Listo';
                boton.disabled = false;
            }, 2000);
        });
    });
});

function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'notification show';
    notification.innerText = message;
    document.body.appendChild(notification);

    // Ocultar la notificación después de 3 segundos
    setTimeout(() => {
        notification.classList.remove('show');
        document.body.removeChild(notification);
    }, 3000);
}

function loadRecomendaciones(proyectoId) {
    fetch(`/recomendaciones/${proyectoId}`)
        .then(response => response.text())
        .then(data => {
            document.getElementById('panel-recomendaciones').innerHTML = data;
        })
        .catch(error => console.error('Error al cargar recomendaciones:', error));
}

function validateForm() {
    let isValid = true;
    const titulo = document.getElementById('titulo');
    const descripcion = document.getElementById('descripcion');
    
    // Validación del campo de título
    if (titulo.value.trim() === "") {
        titulo.classList.add('error');
        isValid = false;
    } else {
        titulo.classList.remove('error');
    }
    
    // Validación del campo de descripción
    if (descripcion.value.trim() === "") {
        descripcion.classList.add('error');
        isValid = false;
    } else {
        descripcion.classList.remove('error');
    }

    return isValid;
}

function loadRecomendaciones(proyectoId) {
    fetch(`/recomendaciones/${proyectoId}`)
        .then(response => response.text())
        .then(data => {
            document.getElementById('panel-recomendaciones').innerHTML = data;
        })
        .catch(error => console.error('Error al cargar recomendaciones:', error));
}
