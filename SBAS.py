from socket import *

direccServidor = "localhost"
puertoServidor = 9099

#Creacion del socket
socketServidor = socket(AF_INET, SOCK_STREAM)
#Establecimiento de la conexion
socketServidor.bind( (direccServidor,puertoServidor))
socketServidor.listen()

while True:
    #Creacion conexion
    socketConexion, addr = socketServidor.accept()
    print("Conectado con el cliente", addr)
    while True:
        #Recepcion del mensaje
        mensajeRecibido=socketConexion.recv(4096).decode()
        print(mensajeRecibido)

        #Condicional para cerrar conexion
        if mensajeRecibido == 'adios':
            break
        #De lo contrario enviar
        socketConexion.send(input().encode())
    
    print("Desconectado del cliente", addr)
    #Cerar conexion
    socketConexion.close()