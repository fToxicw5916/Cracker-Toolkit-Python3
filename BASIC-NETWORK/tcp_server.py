'''
A multithreaded simple TCP server.
'''
# Import needed packages
import socket  # Used for TCP connections
import threading  # Needed for multithreading

# IP and port for the server
IP = '<Your IP here>'
PORT = <Your port here>


def main():
    '''
    Main function.
    '''
    # Create a socket object and bind the IP and port
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, address = server.accept()  # Accept connectiona
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))  # Define a thread
        client_handler.start()  # Start the thread


def handle_client(client_socket):
    '''
    Handle client connections.
    '''
    with client_socket as sock:
        request = sock.recv(1024)  # Receive data
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')  # Send data


if __name__ == '__main__':
    main()
