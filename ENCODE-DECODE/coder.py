#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A simple encoder and decoder made from python.
'''
# Import needed packages
import base64 # Base 64

en_de = input('Encode or decode? ')
en_de = en_de.lower()
coding = input('Way of encoding: ')
coding = coding.lower()
data = input('Data: ')

# Base64 encode
def base64Encode(data):
    data2 = str.encode(data.strip())
    endata = base64.b64encode(data2)
    endata = str(endata)
    endata = endata.strip('b\'')
    print(endata)

# Base64 decode
def base64Decode(data):
    data2 = str.encode(data.strip())
    dedata = base64.b64decode(data2)
    dedata = str(dedata)
    dedata = dedata.strip('b\'')
    print(dedata)

# Main function
def main():
    if en_de == 'encode': # Encode
        # Base 64 encode
        if coding.strip() == 'base64':
            base64Encode(data)
    else: # Decode
        # Base 64 decode
        if coding.strip() == 'base64':
            base64Decode(data)

# Run the program
if __name__ == '__main__':
    main()
