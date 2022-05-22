'''
A Netcat network tool written in Python. You don't need to change anything to run the program, just read the help message if you don't know how to use it. Use CTRL-D to send the EOF (End of file) marker.

Netcat is the utility knife of networking, so it's no surprise that shrewd systems administrators remove it from their systems. Such a useful tool would be quite an asset if an attacker managed to find a way in. With it, you can read and write data across the network, meaning you can use it to execute remote commands, pass files back and forth, or even open a remote shell.
'''
# Import needed packages
import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

# Execute a command
def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd),
                                     stderr=subprocess.STDOUT)
    return output.decode()

# Netcat
class NetCat:
    # Initialize Netcat
    def __init__(self, args, buffer=None):
        self.args = args # Arguments
        self.buffer = buffer
        # Create a socket object
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Run the Netcat
    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

    def send(self):
        self.socket.connect((self.args.target, self.args.port)) # Connect to the server
        if self.buffer:
            self.socket.send(self.buffer)

        try: # You can close the conection by CTRL-C
            while True:
                recv_len = 1
                response = ''
                while recv_len: # Receive data
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096: # If there is no more data, break
                        break
                if response: # Print the response data and get interactive input
                    print(response)
                    buffer = input('> ')
                    buffer += '\n'
                    self.socket.send(buffer.encode()) # Send the input, continue the loop
        except KeyboardInterrupt: # Use CTRL-C to close the connection
            print('User terminated.')
            self.socket.close()
            sys.exit()

    # The server side
    def listen(self):
        print('Listening')
        self.socket.bind((self.args.target, self.args.port)) # Bind the IP and port.
        self.socket.listen(5)
        while True:
            client_socket, _ = self.socket.accept()
            client_thread = threading.Thread(target=self.handle, args=(client_socket,))
            client_thread.start()

    # Performs upload, execute commands, and create interactive shells
    def handle(self, client_socket):
        if self.args.execute: # Execute a file
            output = execute(self.args.execute)
            client_socket.send(output.encode())

        elif self.args.upload: # Upload a file
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                    print(len(file_buffer))
                else:
                    break

            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)
            message = f'Saved file {self.args.upload}'
            client_socket.send(message.encode())

        elif self.args.command: # Execute a command
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b' #> ')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'Server killed {e}')
                    self.socket.close()
                    sys.exit()

# Run the program
if __name__ == '__main__':
    # Get arguments
    parser = argparse.ArgumentParser(
        description='Python Netcat',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
          netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
          netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.whatisup # upload to file
          netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
          echo 'ABCDEFGHI' | ./netcat.py -t 192.168.1.108 -p 135 # echo local text to server port 135
          netcat.py -t 192.168.1.108 -p 5555 # connect to server
          '''))
    parser.add_argument('-c', '--command', action='store_true', help='initialize command shell')
    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
    parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
    parser.add_argument('-u', '--upload', help='upload file')
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()

    # Run!
    nc = NetCat(args, buffer.encode('utf-8'))
    nc.run()
