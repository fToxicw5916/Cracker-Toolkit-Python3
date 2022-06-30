'''
A simple script that returns the files in the current directory.
'''
# Import needed packages
import os


def run(**args):
    '''
    Main function
    '''
    print("[*] In dirlister module.")
    files = os.listdir('.')  # List the files
    return str(files)  # Return the result
