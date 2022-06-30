'''
A web sniffer that reads in a single packet, and exit.
'''
# Import needed packages
import socket
import os

# Your computer
HOST = '127.0.0.1'


def main():
    '''
    Main function.
    '''
    if os.name == 'nt':  # Identify whether the host is Windows or Linux
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        
    print(sniffer.recvfrom(65565))  # Receive data

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    

if __name__ == '__main__':
    main()
