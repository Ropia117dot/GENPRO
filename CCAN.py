from socket import *
import sys
import pygame
import random

IPServidor = "localhost"
puertoServidor = 9099

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
rover_speed = .5

# Puntos de interés (aleatorios)
points_of_interest = [(random.randint(0, width), random.randint(0, height)) for _ in range(3)]

# Se inicializan los valores del socket del cliente
socketCliente = socket(AF_INET, SOCK_STREAM)
socketCliente.connect((IPServidor, puertoServidor))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mensaje = 'i'
        socketCliente.send(mensaje.encode())
        respuesta = socketCliente.recv(4096).decode()
        rover_x, rover_y = map(float, respuesta.split(','))  # Actualiza la posición solo después de recibir la respuesta del servidor
        
    if keys[pygame.K_RIGHT]:
        mensaje = 'd'
        socketCliente.send(mensaje.encode())
        respuesta = socketCliente.recv(4096).decode()
        rover_x, rover_y = map(float, respuesta.split(','))  # Actualiza la posición solo después de recibir la respuesta del servidor
        
    if keys[pygame.K_UP]:
        mensaje = 'ar'
        socketCliente.send(mensaje.encode())
        respuesta = socketCliente.recv(4096).decode()
        rover_x, rover_y = map(float, respuesta.split(','))  # Actualiza la posición solo después de recibir la respuesta del servidor
        
    if keys[pygame.K_DOWN]:
        mensaje = 'bj'
        socketCliente.send(mensaje.encode())
        respuesta = socketCliente.recv(4096).decode()
        rover_x, rover_y = map(float, respuesta.split(','))  # Actualiza la posición solo después de recibir la respuesta del servidor

    # Renderizar canvas
    screen.fill(white)
    for point in points_of_interest:
        pygame.draw.circle(screen, black, point, 5)
    pygame.draw.rect(screen, black, (rover_x, rover_y, 20, 20))
    pygame.display.flip()

pygame.quit()
socketCliente.close()
sys.exit()
