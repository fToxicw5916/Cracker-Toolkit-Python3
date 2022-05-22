'''
This is a simple TCP client made from Python socket package. Change the parameters to your own before running the program. They are already highlighted in the file.

Countless times during penetration tests, we have needed to whip up a TCP client to test for services, send garbage data, fuzz, or perform any number of other tasks. If you are working within the confines of large enterprise environments, you won't have the luxury of using networking tools or compilers, and sometimes you'll even be missing the absolute basics, like the ability to copy/paste or connect to the internet. This is where being able to quickly create a TCP client comes in extreme handy.
'''
# Import needed packages
import socket

# Host and port
HOST = '<Your host here>'
PORT = <Your port here>

# Create a socket object and connect to the server using HOST and PORT
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Send data and receive data
client.send(b'GET / HTTP/1.1\r\nHost: <Your host here>\r\n\r\n')
response = client.recv(4096)
print(response.decode('utf-8'))

# Close the connection
client.close()
