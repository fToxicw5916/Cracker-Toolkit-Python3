'''
A simple UDP client.
'''
# Import needed packages
import socket  # For TCP connections

# Target host and port
HOST = '<Your host here>'
PORT = <Your port here>

# Create a socket object and send some data to the host
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'AAABBBCCC', (HOST, PORT))

# Receive data from the host
data, address = client.recvfrom(4096)
print(data.decode('utf-8'))
print(address.decode('utf-8'))

# Close the connection
client.close()
