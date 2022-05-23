#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A simple Base64 list encoder and decoder made from Python.
'''
# Import needed packages
import base64

en_de = input('Encode or decode? ')
en_de = en_de.lower()
file = input('File: ')

with open(file, 'r') as f:
    datas = f.readlines()

# Encode
def encode(datas):
    for data in datas:
        data2 = str.encode(data.strip())
        endata = base64.b64encode(data2)
        endata = str(endata)
        endata = endata.strip('b\'')
        print(endata)

# Decode
def decode(datas):
    for data in datas:
        data2 = str.encode(data.strip())
        dedata = base64.b64decode(data2)
        dedata = str(dedata)
        dedata = dedata.strip('b\'')
        print(dedata)

def main():
    if en_de == 'encode':
        # Encode
        encode(datas)
    else:
        # Decode
        decode(datas)

if __name__ == '__main__':
    main()
