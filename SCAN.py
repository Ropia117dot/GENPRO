from socket import *

direccServidor = "localhost"
puertoServidor = 9099
width, height = 800, 600
rover_x, rover_y = width // 2, height // 2
rover_speed = .5

# Creación del socket
socketServidor = socket(AF_INET, SOCK_STREAM)
# Establecimiento de la conexión
socketServidor.bind((direccServidor, puertoServidor))
socketServidor.listen()

while True:
    # Creación conexión
    socketConexion, addr = socketServidor.accept()
    print("Conectado con el cliente", addr)
    while True:
        # Recepción del mensaje
        mensajeRecibido = socketConexion.recv(4096).decode()
        if not mensajeRecibido:
            break
        if mensajeRecibido == 'i':
            rover_x -= rover_speed
        elif mensajeRecibido == 'd':
            rover_x += rover_speed
        elif mensajeRecibido == 'ar':
            rover_y -= rover_speed
        elif mensajeRecibido == 'bj':
            rover_y += rover_speed
        else:
            break
        # Enviar la nueva posición al cliente
        socketConexion.send(f"{rover_x},{rover_y}".encode())
        print(f"Recibido: {mensajeRecibido} - Nueva posición: {rover_x}, {rover_y}")
    print("Desconectado del cliente", addr)
    # Cerrar conexión
    socketConexion.close()
