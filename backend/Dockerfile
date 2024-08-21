# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY requirements.txt ./
COPY run.py ./
COPY app/ ./app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que la aplicación escuchará
EXPOSE 8888

# Define el comando para ejecutar tu aplicación
CMD ["python", "run.py"]
