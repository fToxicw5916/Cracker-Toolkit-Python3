'''
The reverse for ssh_cmd.py
'''
# Import needed packages
import paramiko # INSTALL BEFORE USE!
import shlex
import subprocess


def ssh_command(ip, port, user, passwd, command):
    '''
    Create a SSH object, and send the command to the client.
    '''
    client = paramiko.SSHClient()  # Create a SSH client
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print(ssh_session.recv(1024).decode())  # Read banner
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


if __name__ == '__main__':
    import getpass  # Needed to hide password
    user = getpass.getuser()
    password = getpass.getpass()  # Hide the password during the input

    ip = input('Enter server IP: ')
    port = input('Enter port: ')
    ssh_command(ip, port, user, password, 'ClientConnected')
