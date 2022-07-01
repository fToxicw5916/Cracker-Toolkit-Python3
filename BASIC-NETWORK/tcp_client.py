'''
A simple TCP client.
'''
# Import needed packages
import socket  # For TCP connections

# Target host and port
HOST = '<Your host here>'
PORT = <Your port here>

# Create a socket object and connect to the server using HOST and PORT
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create object
client.connect((HOST, PORT))  # Connect

# Send data and receive data
client.send(b'GET / HTTP/1.1\r\nHost: <Your host here>\r\n\r\n')  # Send data
response = client.recv(4096)  # Receive data
print(response.decode('utf-8'))  # Print decoded data

client.close()  # Close the connection
