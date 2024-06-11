# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos y el archivo de descarga de NLTK al contenedor
COPY requirements.txt .
COPY nltk_download.py .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Ejecuta el script de descarga de NLTK
RUN python nltk_download.py

# Copia el resto de los archivos del proyecto al contenedor
COPY . .

# Establece las variables de entorno necesarias (ajusta según sea necesario)
ENV OPENAI_API_KEY=<tu_openai_api_key>
ENV DISCORD_TOKEN=<tu_discord_token>

# Comando para ejecutar el bot
CMD ["python", "main.py"]
