#--------------------------------------------------
#Tarea 1 Ejemplo Cliente servidor
#chat bidimensional cliente servidor
#py Servidor
#--------------------------------------------------
import socket # por medio de socket  cliente servidor se corren localmente
com = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #establecemos una comunicacion tcp/ip
com.bind(("", 9798)) #HOST, PUERTO
com.listen(3) #cantidad de clientes que manejara el servidor
print("------------------------------------")
print("CHAT DEL SERVIDOR:")
print("------------------------------------\n")
active, add = com.accept() # aqui se establece la conexión
try:
    while True:
        mRecibido = active.recv(1024) #se le asigna la conexión  en escucha
        print("Cliente: ", mRecibido.decode('utf-8')) # cuando llegue un mensaje se imprime y e decodifica como utf8 
        mEnviado = input('Tú: ') #esto es lo que enviamos al cliente
        active.send(mEnviado.encode('utf-8')) #lo codificamos como utf 8
except:
    print("Fin de la comunicación")