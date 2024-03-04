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

# Función para ajustar el tiempo del nodo esclavo según la diferencia de tiempo recibida del nodo maestro
def ajustar_tiempo(tiempo_maestro, diferencia_tiempo):
    return tiempo_maestro + diferencia_tiempo

# Función principal
def main():
    # Configurar el cliente del nodo esclavo
    host = 'localhost'
    puerto = 12345

    # Crear un objeto de socket TCP/IP
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar el cliente al nodo maestro a través del host y puerto especificados
    cliente.connect((host, puerto))

    # Recibir el tiempo actual del nodo maestro
    tiempo_maestro = float(cliente.recv(1024).decode())
    print("Tiempo recibido del nodo maestro:", tiempo_maestro)

    # Enviar el tiempo actual del nodo esclavo al nodo maestro
    tiempo_actual = obtener_tiempo_actual()
    cliente.send(str(tiempo_actual).encode())

    # Recibir la diferencia de tiempo calculada por el nodo maestro
    diferencia_tiempo = float(cliente.recv(1024).decode())
    print("Diferencia de tiempo recibida del nodo maestro:", diferencia_tiempo)

    # Ajustar el tiempo del nodo esclavo utilizando la diferencia de tiempo y mostrarlo
    tiempo_ajustado = ajustar_tiempo(tiempo_maestro, diferencia_tiempo)
    print("Tiempo ajustado del nodo esclavo:", tiempo_ajustado)

    # Cerrar la conexión con el nodo maestro
    cliente.close()

# Ejecutar la función principal si este script es el archivo principal
if __name__ == "__main__":
    main()
