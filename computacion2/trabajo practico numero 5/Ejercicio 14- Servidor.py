import socket
import sys
import getopt

def main(argv):
    port = 0
    protocol = ''
    file_path = ''
    
    try:
        opts, _ = getopt.getopt(argv, "p:t:f:", [])
    except getopt.GetoptError:
        print("Usage: servidor.py -p <port> -t <tcp/udp> -f <file_path>")
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == "-p":
            port = int(arg)
        elif opt == "-t":
            protocol = arg
        elif opt == "-f":
            file_path = arg
    
    if not port or not protocol or not file_path:
        print("Usage: servidor.py -p <port> -t <tcp/udp> -f <file_path>")
        sys.exit(2)
    
    if protocol != 'tcp' and protocol != 'udp':
        print("Invalid protocol. Use 'tcp' or 'udp'.")
        sys.exit(2)

    try:
        with open(file_path, 'w') as file:
            file.write('')
    except Exception as e:
        print(f"Error creating file: {e}")
        sys.exit(2)

    if protocol == 'tcp':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server_address = ('', port)
    sock.bind(server_address)
    sock.listen(1)

    print(f"Waiting for a connection on port {port}...")
    connection, client_address = sock.accept()
    print("Connection established with:", client_address)
    
    with open(file_path, 'wb') as file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            file.write(data)
    
    connection.close()
    sock.close()

if __name__ == "__main__":
    main(sys.argv[1:])
