"""
Código desarrollado por:

- Genis Cruz Lourdes Victoria (Número de cuenta: 420053978)
- Montes Cantero Zelene Yosseline Isayana (Número de cuenta: 317159923)
- Peñafiel Garcés Abigail (Número de cuenta: 317119093)
- Recinos Hernández Luis Mario (Número de cuenta: 317244331)

Materia: Sistemas Distribuidos
Facultad: Ingeniería
Institución: Universidad Nacional Autónoma de México (UNAM)

Fecha: 28 de febrero de 2024
"""

# Importar las bibliotecas necesarias
import socket
import time

# Función para obtener el tiempo actual en segundos
def obtener_tiempo_actual():
    return time.time()

# Función para enviar el tiempo actual a través del socket
def enviar_tiempo(socket_cliente):
    tiempo_actual = obtener_tiempo_actual()
    mensaje = str(tiempo_actual)
    socket_cliente.send(mensaje.encode())

# Función principal
def main():
    # Configurar el servidor del nodo maestro
    host = 'localhost'
    puerto = 12345

    # Crear un objeto de socket TCP/IP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincular el socket al host y puerto especificados
    servidor.bind((host, puerto))

    # Configurar el socket para escuchar hasta 5 conexiones en espera
    servidor.listen(5)

    print("Esperando conexiones de nodos esclavos en el puerto", puerto)

    # Aceptar la conexión del primer nodo esclavo   
    cliente, direccion = servidor.accept()
    print("Conexión establecida desde", direccion)

    # Enviar el tiempo actual al nodo esclavo
    enviar_tiempo(cliente)

    # Esperar la respuesta del nodo esclavo
    tiempo_esclavo = float(cliente.recv(1024).decode())
    print("Tiempo recibido del nodo esclavo:", tiempo_esclavo)

    # Calcular la diferencia de tiempo y enviarla al nodo esclavo
    diferencia_tiempo = obtener_tiempo_actual() - tiempo_esclavo
    cliente.send(str(diferencia_tiempo).encode())

    # Cerrar la conexión con el nodo esclavo
    cliente.close()
    servidor.close()

# Ejecutar la función principal si este script es el archivo principal
if __name__ == "__main__":
    main()