# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo del servidor al contenedor
COPY SCAN.py /app/SCAN.py

# Instalar dependencias necesarias
RUN pip install --no-cache-dir requests

# Exponer el puerto en el que escucha el servidor
EXPOSE 9099

# Comando para ejecutar el servidor
CMD ["python", "SCAN.py"]
