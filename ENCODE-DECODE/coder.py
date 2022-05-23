#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A simple Base64 encoder and decoder made from Python.
'''
# Import needed packages
import base64

en_de = input('Encode or decode? ')
en_de = en_de.lower()
data = input('Data: ')

# Encode
def encode(data):
    data2 = str.encode(data.strip())
    endata = base64.b64encode(data2)
    endata = str(endata)
    endata = endata.strip('b\'')
    print(endata)

# Decode
def decode(data):
    data2 = str.encode(data.strip())
    dedata = base64.b64decode(data2)
    dedata = str(dedata)
    dedata = dedata.strip('b\'')
    print(dedata)

# Main function
def main():
    if en_de == 'encode': # Encode
        # Encode
        encode(data)
    else: # Decode
        # Decode
        decode(data)

# Run the program
if __name__ == '__main__':
    main()
