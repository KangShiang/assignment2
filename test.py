__author__ = 'KangShiang'
import binascii
import string
import random

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

dict = {}
boole = 1

while(boole==1):
    key = id_generator()
    hash = binascii.crc32(key)
    if key in dict:
        print(str(dict[hash])+":"+str(key))
        print(str(key)+":"+str(hash))
        boole = 1
    else:
        dict[hash]=key
