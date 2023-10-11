# api3Django
## Propósito
El propósito principal de api3Django es proporcionar una herramienta eficiente para:

Gestión de Profesores: Permite la gestión de profesores, su información personal y su relación con la plataforma mediante la extensión de la clase de usuario proporcionada por Django.

Horarios y Períodos Académicos: Facilita la programación y asignación de clases para profesores en diferentes períodos académicos, con la capacidad de ajustar la duración de los periodos según la temporada.

Asignaturas: Ofrece un sistema para administrar y asignar asignaturas a los horarios, lo que permite un control preciso de qué se enseña en cada período.

Horas Hábiles: Ayuda en la gestión de las horas hábiles, permitiendo que los períodos académicos se adapten a las necesidades específicas de la institución.

En resumen, api3Django simplifica la gestión de la información académica y los horarios en una unidad educativa, lo que ahorra tiempo y recursos valiosos, y garantiza una organización más eficiente de la actividad educativa.

¡Esperamos que api3Django sea una herramienta útil para tu unidad educativa y contribuya a una gestión académica efectiva!

## Requisitos Previos

Asegúrate de tener instalados los siguientes requisitos previos antes de comenzar:

- Python (versión 3.10.12)
- Pip (Version 22.0.2 el gestor de paquetes de Python)

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone git@github.com:aorosco/api3Django.git

2. Ve al directorio del proyecto:
   ```bash
   cd api3Django
3. Crea un entorno virtual para el proyecto:
   ```bash
   python -m venv venv
4. Activa el entorno virtual en macOS y Linux::
   ```bash
   source venv/bin/activate
5. Activa el entorno virtual en Windows::
   ```bash
   venv\Scripts\activate
6. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
7. Realiza las migraciones de la base de datos:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

8. Crea un superusuario para administrar el proyecto:
   ```bash
   python manage.py createsuperuser
9. Inicia el servidor de desarrollo e 
   ```bash
   python manage.py runserver
10. ingresa a la ruta:
   http://localhost:8000/

#  Para el inicio de sesión en http://localhost:8000/api/token/  se requiere crear una cuenta por medio del administrador de Django ( http://localhost:8000/admin/   ) o también puedes usar las credenciales de la cuenta de administrador que se creó en el paso número  8. 


