== Listado_pendientes
Este proyecto es una aplicación web de gestión de tareas (ToDo) desarrollada con Django. Permite importar tareas desde una API pública.

== Características

- Importa tareas desde la API pública [JSONPlaceholder](https://jsonplaceholder.typicode.com/todos).
- CRUD completo para tareas locales.
- Filtrado de tareas por estado (resueltas/no resueltas) y por usuario.
- Vistas para mostrar diferentes combinaciones de datos (ID, título, usuario, estado).
- Interfaz web sencilla para la gestión de tareas.

== Requisitos

- Python 3.8 o superior
- Django 4.x
- requests

== Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Contreras-Yael/Listado_pendientes.git
   cd Listado_pendientes
   ```

2. Crea un entorno virtual (opcional pero recomendado)
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install django requests
   ```

4. Realiza las migraciones de la base de datos:
   ```bash
   python manage.py migrate
   ```

5. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

6. Accede a la aplicación:
   Abre tu navegador y entra a [http://localhost:8000/](http://localhost:8000/)

== Uso

- Para importar tareas desde la API externa, accede a la ruta `/importar_api/` (puedes enlazarla en tu menú o llamarla manualmente).
- Usa las diferentes vistas para ver tareas filtradas por estado, usuario, etc.
- Gestiona tus tareas locales desde la interfaz web.

== Estructura del Proyecto

- `ToDo/views.py`: Vistas y uso de API externa.
- `ToDo/models.py`: Modelo de datos para las tareas.
- `ToDo/templates/todo/`: Plantillas HTML para las vistas.

== Notas

- Este proyecto utiliza la API pública [JSONPlaceholder](https://jsonplaceholder.typicode.com/todos) solo para pruebas y demostraciones.
- Este proyecto es solo para fines educativos y de demostración.

---
