#--------------------------------------------------
#Tarea 1 Ejemplo Cliente servidor
#chat bidimensional cliente servidor
#py cliente
#--------------------------------------------------
import socket # por medio de socket   cliente servidor se corren localmente
print("------------------------------------")
print("CHAT DEL CLIENTE:")
print("------------------------------------")
# este es el puerto e ip del servidor
servidorPuerto =9798
servidorIp="localhost"
cliente= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((servidorIp,servidorPuerto))
print("Ruta del Servidor:", (servidorIp,servidorPuerto),"\n")
try:
    while True:
        mEnviado = input("Tú: ")
        if mEnviado !='salir':
            cliente.send(mEnviado.encode('utf-8'))
            mRecibido=cliente.recv(1024)
        if mEnviado=='salir':
            mEnviado ='El cliente salio'
            cliente.send(mEnviado.encode('utf-8'))
            break
        print ("Servidor: ", mRecibido.decode('utf-8'))
except:
    print("Fin de la comunicación")
