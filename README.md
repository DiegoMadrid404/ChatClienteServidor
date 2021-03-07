#Especialización en Ingeniría de Software
#Informatica I
#Tarea 1 : Ejemplo Simple Cliente-Servidor o Capas

#Integrantes:
Luz Amanda Quilindo
Diego Alejandro Madrid
Juan Sebastian Vega

#ChatClienteServidor
Programa Python con arquitectura Cliente servidor, usando socket para una comunicación bidireccional.





#¿Cómo instalar la aplicación?
1) Esta aplicacion esta compuesta por dos parte (Cliente-Servidoor), una vez clonado el repositorio
debes ejecutar en primera instancia el Servidor (servidor.py)
		python servidor.py
		
2) Ejecutar el Cliente (cliente.py) en la consola
		python cliente.py
		
3) Para salir de la aplicación el cliente debe digitar la palabra "Salir"

Nota: Antes de correr el cliente en la consola de comando, asegurarse de que el puerto seleccionado
se encuentre libre para ser usado por la aplicación.

#Ventajas Arquitectura CLiente - Servidor

1) Los accesos, recursos y la integridad de los datos con controlados por el servidor de la arquitectura,
de forma que podemos centralizar la información de la empresa o compañía en un solo punto al cual los clientes
tienen que acceder para consultar.

2) El estado de los clientes (defectuoso o caído) no afecta el servidor dentro de la arquitectura, el servidor
puede continuar funcionando de independiente de la cantidad de clientes o el estado de los mismos.

3) Se puede aumentar la capacidad de clientes y servidores por separado. Cualquier elemento puede ser aumentado 
(o mejorado) en cualquier momento, o se pueden añadir nuevos nodos a la red (clientes y/o servidores).

4) Al poseer esta misma arquitectura de forma distribuida las funciones y responsabilidades entre varios ordenadores
independientes, es posible reemplazar, actualizar, reparar o incluso trasladar un servidor, sin ver afectados a sus
clientes.

5) Existen tecnologías, suficientemente desarrolladas, diseñadas para el paradigma de C/S que aseguran
la seguridad en las transacciones, la amigabilidad del interfaz, y la facilidad de empleo.

6) La capacidad de proceso está repartida entre los clientes y los servidores.

#Desventajas Arquitectura CLiente - Servidor

1) Varios clientes pueden comenzar a enviar peticiones al servidor de forma que lo comienzan a saturar,
de esta manera el servidor cae por sobre cargar de peticiones sin poder atender.

2) El servidor de la arquitectura posee toda la información de la aplicación que desean consultar los clientes,
si el servidor es desconectado o cae por fallas en el sistema, los clientes no podrán consultar los datos.

3) El hecho que se comparte canales de información entre servidores y clientes requieren que estas pasen por
procesos de validación, es decir protocolos de seguridad que pueden tener algún tipo de puerta abierta 
permitiendo que se generen daños físicos, amenazas o ataques de malware.

4) Representa una limitación importante en cuanto a los costos económicos debido a que estos servidores son
computadoras de alto nivel con un hardware y software específicos para poder dar un correcto funcionamiento
a nuestras aplicaciones.

![image](https://user-images.githubusercontent.com/80139895/110247939-a650a380-7f3c-11eb-9d74-6e07163278f3.png)

