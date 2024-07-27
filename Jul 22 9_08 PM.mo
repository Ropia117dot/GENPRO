//PROGRAMA DEL CLIENTE//

import pygame
import requests
import random

# Inicializar Pygame
pygame.init()

# Dimensiones del canvas
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Posición inicial del rover
rover_x, rover_y = width // 2, height // 2
rover_speed = 10

# Puntos de interés (aleatorios)
points_of_interest = [(random.randint(0, width), random.randint(0, height)) for _ in range(3)]

# Función para enviar datos al servidor
def send_data_to_server(data):
    try:
        response = requests.post('http://<SERVER_IP>:<PORT>/api', json=data)
        return response.json()
    except Exception as e:
        print(f"Error sending data to server: {e}")
        return None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rover_x -= rover_speed
        send_data_to_server({"action": "move", "direction": "left", "position": {"x": rover_x, "y": rover_y}})
    if keys[pygame.K_RIGHT]:
        rover_x += rover_speed
        send_data_to_server({"action": "move", "direction": "right", "position": {"x": rover_x, "y": rover_y}})
    if keys[pygame.K_UP]:
        rover_y -= rover_speed
        send_data_to_server({"action": "move", "direction": "up", "position": {"x": rover_x, "y": rover_y}})
    if keys[pygame.K_DOWN]:
        rover_y += rover_speed
        send_data_to_server({"action": "move", "direction": "down", "position": {"x": rover_x, "y": rover_y}})
    if keys[pygame.K_RETURN]:
        for point in points_of_interest:
            if abs(rover_x - point[0]) < 10 and abs(rover_y - point[1]) < 10:
                # Simular toma de fotografía
                photo_data = {"photo": "data:image/png;base64,..."}  # Simulación de foto
                send_data_to_server({"action": "photo", "data": photo_data, "position": {"x": rover_x, "y": rover_y}})

    # Renderizar canvas
    screen.fill(white)
    for point in points_of_interest:
        pygame.draw.circle(screen, black, point, 5)
    pygame.draw.rect(screen, black, (rover_x, rover_y, 20, 20))
    pygame.display.flip()

pygame.quit()


//PROGRAMA DEL SERVIDOR//
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configuración de logging
logging.basicConfig(filename='server.log', level=logging.INFO)

@app.route('/api', methods=['POST'])
def api():
    data = request.json
    action = data.get('action')
    if action == 'move':
        direction = data.get('direction')
        position = data.get('position')
        logging.info(f'Move action: {direction} to position {position}')
        return jsonify({"status": "success", "action": "move", "direction": direction, "position": position})
    elif action == 'photo':
        photo_data = data.get('data')
        position = data.get('position')
        logging.info(f'Photo action received at position {position}')
        # Validar código ARUCO aquí
        return jsonify({"status": "success", "action": "photo", "position": position})
    return jsonify({"status": "error", "message": "Invalid action"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


//DOCKERFILE QUE PIDEN//
# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos requeridos
COPY . /app

# Instalar las dependencias
RUN pip install flask

# Exponer el puerto que usará la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "Servidor.py"]
