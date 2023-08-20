import socket
import sys
import getopt

def main(argv):
    server_address = ''
    port = 0
    protocol = ''

    try:
        opts, _ = getopt.getopt(argv, "a:p:t:", [])
    except getopt.GetoptError:
        print("Usage: cliente.py -a <server_address> -p <port> -t <tcp/udp>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-a":
            server_address = arg
        elif opt == "-p":
            port = int(arg)
        elif opt == "-t":
            protocol = arg
    
    if not server_address or not port or not protocol:
        print("Usage: cliente.py -a <server_address> -p <port> -t <tcp/udp>")
        sys.exit(2)
    
    if protocol != 'tcp' and protocol != 'udp':
        print("Invalid protocol. Use 'tcp' or 'udp'.")
        sys.exit(2)
    
    try:
        if protocol == 'tcp':
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.connect((server_address, port))
    except Exception as e:
        print(f"Error connecting to the server: {e}")
        sys.exit(2)

    print("Connected to the server. Start typing (Ctrl+d to send):")

    try:
        while True:
            data = input()
            sock.sendall(data.encode())
    except EOFError:
        sock.close()
        print("Data sent successfully.")

if __name__ == "__main__":
    main(sys.argv[1:])
