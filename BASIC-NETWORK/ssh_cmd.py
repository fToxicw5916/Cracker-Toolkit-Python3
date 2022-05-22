#!/usr/bin/env python

'''
A SSH tool built with Python.

The Netcat tool we built is pretty handy, but sometimes it's wise to encrypt your traffic to avoid detection. A common means of doing so is to tunnel the traffic using Secure Shell (SSH). But what if your target doesn't have an SSH client, just like 99.81943 percent of Windows systems? That is why we will need to build a SSH tool using Python.
'''
# Import needed packages
import paramiko # Use "pip install paramiko" to install the package

# Create a SSH Client, connect to the host, and send the command.
def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('--- Output ---')
        for line in output:
            print(line.strip())

# Run the program
if __name__ == '__main__':
    import getpass # Needed for hiding password
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass() # Hide password during the input

    ip = input('Enter server IP: ') or '127.0.0.1'
    port = input('Enter port or <CR>: ') or 2222
    cmd = input('Enter command or <CR>: ') or 'id'
    ssh_command(ip, port, user, password, cmd)
