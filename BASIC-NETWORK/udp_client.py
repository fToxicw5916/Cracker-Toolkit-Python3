'''
A simple UDP client.
'''
# Import needed packages
import socket  # For TCP connections

# Target host and port
HOST = '<Your host here>'
PORT = <Your port here>

# Create a socket object and send some data to the host
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create object
client.sendto(b'AAABBBCCC', (HOST, PORT))  # Connect & Send data

# Receive data from the host
data, address = client.recvfrom(4096)  # Receive data
print(data.decode('utf-8'))  # Decode data
print(address.decode('utf-8'))  # Decode data

client.close()  # Close the connection
