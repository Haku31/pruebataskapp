# Task List Application

¡Bienvenido a la aplicación de gestión de tareas! Esta aplicación te permite administrar tus tareas de manera eficiente mediante una API que soporta operaciones CRUD (Crear, Leer, Actualizar, Eliminar). Está compuesta por un backend en Python utilizando Tornado y un frontend en React, y está completamente contenedorizada usando Docker para facilitar su despliegue y gestión.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes en tu máquina:

- Docker Desktop
- Docker

## Clonación del Repositorio

Para clonar el repositorio, abre una terminal y ejecuta:

```bash
git clone https://github.com/Haku31/pruebataskapp.git
cd pruebataskapp
```

## Ejecución con Docker Compose

Para iniciar la aplicación, ejecuta el siguiente comando en la raíz del proyecto:

```bash
docker compose up
```

Una vez que Docker Compose haya iniciado los contenedores, el backend estará disponible en el puerto 8888 y el frontend en el puerto 3000. Puedes acceder a la aplicación en tu navegador en localhost:3000.

## Activación del Entorno Python y Pruebas

Si deseas ejecutar pruebas en el backend, sigue estos pasos:


### Activa el entorno virtual:

En Windows:

```bash
venv\Scripts\activate
```
Regresa al directorio raíz del proyecto y ejecuta las pruebas:

```bash
cd ..
pytest
```
### ¡Disfruta del Software!
### ¡Eso es todo! Ahora puedes disfrutar de tu aplicación de gestión de tareas. Si tienes alguna duda o necesitas asistencia, no dudes en comunicarte con nosotros a: barretojhonalex@gmail.com.



