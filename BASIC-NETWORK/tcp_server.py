'''
A multithreaded simple TCP server written in Python with socket and threading package. Change the parameters highlighted in the file to your own before running it.

You might want to use your own TCP server when writing command shells or crafting a proxy.
'''
# Import needed packages
import socket
import threading # Needed for multithreading

# IP and port for the server
IP = '<Your IP here>'
PORT = <Your port here>

# Main function
def main():
    # Create a socket object and bind the IP and port
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, address = server.accept() # Accept connectiona
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,)) # Define a thread
        client_handler.start() # Start the thread

# What to do when a client connected to the server
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024) # Receive data
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK') # Send data

# Run the program
if __name__ == '__main__':
    main()
