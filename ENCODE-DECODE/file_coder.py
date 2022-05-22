#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

en_de = input('Encode or decode? ')
en_de = en_de.lower()
encode = input('Way of coding: ')
encode = encode.lower()
file = input('File: ')

with open(file, 'r') as f:
    datas = f.readlines()

def main():
    if en_de == 'encode':
        # Base 64 encode
        if encode.strip() == 'base64':
            for data in datas:
                data2 = str.encode(data.strip())
                endata = base64.b64encode(data2)
                endata= str(endata)
                endata = endata.strip('b\'')
                print(endata)

if __name__ == '__main__':
    main()
