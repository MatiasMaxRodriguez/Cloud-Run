# Lab Cloud Run

Laboratorio de Google Cloud Run: Se realiza un deploy en Cloud Run de un container de Docker con un microservicio (página web estática sencilla) con Python y Flask. Para el container de Docker se utiliza una imagen de Phyton 3.11, Flask 3.0 como framework para la creación de la página y CSS para el diseño de la página.

Se trabajó con la siguiente jerarquía de directorios y archivos desde Cloud Shell en GCP:

  * Dockerfile: Configuración básica para el build del container Docker
  * app.py: Lógica principal de Flask
  * requirements: Versión de Flask
  * templates/index.html: Página estática de prueba
  * static/style.css: Diseño de página de prueba
  * comandos_instrucciones.txt: Archivo con los comandos e instrucciones para realizar el deploy de prueba en Cloud Run


## Vista previsual del proyecto

![previsual del proyecto](https://github.com/MatiasMaxRodriguez/Cloud-Run/blob/main/crlab.gif)

## Tecnologías utilizadas:

[Google Cloud Run](https://cloud.google.com/run?hl=es)
[Docker](https://www.docker.com/)
[Python](https://www.python.org/)
[Flask](https://flask.palletsprojects.com/en/stable/)
[HTML](https://html.spec.whatwg.org/multipage/)
[CSS](https://www.w3.org/TR/css/#css)
