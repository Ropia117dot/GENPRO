from socket import *
import sys


IPServidor = "localhost"
puertoServidor = 9099

#Se inicializan los valores del socket del cliente
socketCliente = socket(AF_INET, SOCK_STREAM)
socketCliente.connect((IPServidor,puertoServidor))

while True:

    #Escritura del menasje
    mensaje = input()
    if mensaje != 'adios':
        #Envio del mensaje
        socketCliente.send(mensaje.encode())
        #Recepcion del mensaje
        respuesta= socketCliente.recv(4096).decode()
        print(respuesta)
    else:
        socketCliente.send(mensaje.encode())
        #Cierre del socket
        socketCliente.close()
        sys.exit()