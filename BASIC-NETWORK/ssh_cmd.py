'''
A SSH tool to run commands in remote host.
'''
# Import needed packages
import paramiko  # Install before use!


def ssh_command(ip, port, user, passwd, cmd):
    '''
    Create a SSH Client, connect to the host, and send the command to be executed.
    '''
    client = paramiko.SSHClient()  # Create SSH client
    # Add SSH key
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('--- Output ---')
        for line in output:
            print(line.strip())


if __name__ == '__main__':
    import getpass  # Needed for hiding password
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass() # Hide password during the input

    ip = input('Enter server IP: ') or '127.0.0.1'
    port = input('Enter port or <CR>: ') or 12345
    cmd = input('Enter command or <CR>: ') or 'id'
    ssh_command(ip, port, user, password, cmd)
