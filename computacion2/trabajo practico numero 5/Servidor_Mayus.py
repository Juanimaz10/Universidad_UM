import socket
import argparse

def main():
    parser = argparse.ArgumentParser(description='Servidor para convertir texto a mayúsculas')
    parser.add_argument('-p', '--port', type=int, help='Puerto en el que debe atender el servicio', required=True)
    args = parser.parse_args()

    # Configurar el socket del servidor
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(('0.0.0.0', args.port))
    servidor_socket.listen(1)

    print(f'Esperando conexiones en el puerto {args.port}...')
    conexion, direccion = servidor_socket.accept()
    print(f'Conexión establecida desde {direccion}')

    # Recibir datos del cliente
    datos = conexion.recv(1024).decode('utf-8')
    print(f'Recibido: {datos}')

    # Convertir a mayúsculas
    datos_mayusculas = datos.upper()

    # Enviar datos convertidos al cliente
    conexion.send(datos_mayusculas.encode('utf-8'))
    print(f'Datos convertidos enviados: {datos_mayusculas}')

    # Cerrar la conexión
    conexion.close()
    servidor_socket.close()

if __name__ == "__main__":
    main()
