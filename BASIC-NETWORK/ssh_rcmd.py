#!/usr/bin/env python

'''
The reverse for ssh_cmd.py

Modified ssh_cmd.py so that it can run commands on Windows client over SSH. Because most versions of Windows don't include an SSH server out of the box, we need to reverse ssh_cmd.py and send commands from an server to the client.
'''
# Import needed packages
import paramiko # Use "pip install paramiko" to install the package
import shlex
import subprocess

# Create a SSH object, and send the command to the client
def ssh_command(ip, port, user, passwd, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print(ssh_session.recv(1024).decode())  # read banner
        while True:
            command = ssh_session.recv(1024)
            try:
                cmd = command.decode()
                if cmd == 'exit':
                    client.close()
                    break
                cmd_output = subprocess.check_output(cmd, shell=True)
                ssh_session.send(cmd_output or 'okay')
            except Exception as e:
                ssh_session.send(str(e))
        client.close()
    return

# Run the program
if __name__ == '__main__':
    import getpass # Needed to hide password
    user = getpass.getuser()
    password = getpass.getpass() # Hide the password during the input

    ip = input('Enter server IP: ')
    port = input('Enter port: ')
    ssh_command(ip, port, user, password, 'ClientConnected')
