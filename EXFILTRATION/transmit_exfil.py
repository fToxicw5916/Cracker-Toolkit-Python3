'''
A script that transfer a file using FTP.
'''
# Import needed packages
import ftplib  # FTP file transfer
import os
import socket
import win32file


def plain_ftp(docpath, server='127.0.0.1'):
    '''
    Just normal FTP.
    '''
    ftp = ftplib.FTP(server)
    ftp.login("<Username here!>", "<Email here!>")  # Login to a FTP server
    ftp.cwd('/pub/')  # Change to another directory
    ftp.storbinary("STOR " + os.path.basename(docpath), open(docpath, "rb"), 1024)
    ftp.quit()  # Quit the server


def transmit(document_path):
    '''
    Transfer a file using socket.
    '''
    client = socket.socket()
    client.connect(('192.168.1.207', 10000))
    with open(document_path, 'rb') as f:
        win32file.TransmitFile(
            client,
            win32file._get_osfhandle(f.fileno()),
            0, 0, None, 0, b'', b'')


if __name__ == '__main__':
    transmit('<File to transmit here!>')
