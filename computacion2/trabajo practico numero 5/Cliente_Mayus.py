import socket
import argparse

def main():
    parser = argparse.ArgumentParser(description='Cliente para enviar texto al servidor y recibirlo en mayúsculas')
    parser.add_argument('-a', '--address', type=str, help='Dirección IP del servidor', required=True)
    parser.add_argument('-p', '--port', type=int, help='Puerto del servidor', required=True)
    args = parser.parse_args()

    
    texto = input('Introduzca una cadena de texto: ')

  
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((args.address, args.port))

    
    cliente_socket.send(texto.encode('utf-8'))

    
    datos_mayusculas = cliente_socket.recv(1024).decode('utf-8')
    print(f'Datos en mayúsculas recibidos: {datos_mayusculas}')

    
    cliente_socket.close()

if __name__ == "__main__":
    main()
