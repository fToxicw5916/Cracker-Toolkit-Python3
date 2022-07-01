'''
A Netcat network tool
'''
# Import needed packages
import argparse  # Used for getting arguments
import socket  # Used for TCP connections
import shlex
import subprocess
import sys  # System control
import textwrap
import threading  # Multithread


def execute(cmd):
    '''
    Execute a command.
    '''
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd),
                                     stderr=subprocess.STDOUT)  # Run the command
    return output.decode()  # Return the result


class NetCat:
    '''
    Main class.
    '''
    def __init__(self, args, buffer=None):
        '''
        Initialize Netcat.
        '''
        self.args = args  # Arguments
        self.buffer = buffer  # Current buffer
        # Create a socket object
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        
    # Run Netcat
    def run(self):
        if self.args.listen:
            self.listen()  # As a server
        else:
            self.send()  # As a client

            
    def send(self):
        '''
        Send data.
        '''
        self.socket.connect((self.args.target, self.args.port))  # Connect to the server
        if self.buffer:
            self.socket.send(self.buffer)  # Send the buffer to the target

        try:  # You can close the conection by CTRL-C
            while True:
                recv_len = 1
                response = ''
                while recv_len:  # Receive data
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:  # If there is no more data, break
                        break
                if response:  # Print the response data and get interactive input
                    print(response)
                    buffer = input('> ')
                    buffer += '\n'
                    self.socket.send(buffer.encode())  # Send the input, continue the loop
        except KeyboardInterrupt:  # Use CTRL-C to close the connection
            print('User terminated.')
            self.socket.close()
            sys.exit()  # Exit


    def listen(self):
        '''
        Server side to listen for data.
        '''
        print('Listening')
        self.socket.bind((self.args.target, self.args.port))  # Bind the IP and port.
        self.socket.listen(5)  # Listen for connections
        while True:
            client_socket, _ = self.socket.accept()  # Accept connections
            client_thread = threading.Thread(target=self.handle, args=(client_socket,))  # Define thread for the connecting client
            client_thread.start()  # Start a new thread


    def handle(self, client_socket):
        '''
        Perform tasks.
        '''
        if self.args.execute:  # Execute a file
            output = execute(self.args.execute)  # Get output
            client_socket.send(output.encode())  # Send output

        elif self.args.upload:  # Upload a file
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)  # Receive data/file
                if data:
                    file_buffer += data  # Receive the file
                    print(len(file_buffer))  # Output the file
                else:
                    break

            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)  # Save the file
            message = f'Saved file {self.args.upload}'
            client_socket.send(message.encode())

        elif self.args.command:  # Execute a command
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b' #> ')  # Send command
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
          '''))  # Help message
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
