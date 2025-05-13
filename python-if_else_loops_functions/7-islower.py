#!/usr/bin/python3
def islower(c):
    numero = ord(c)
    if (numero >= 65 and numero < 90):
        print("{} is upper".format(chr(numero)))
    elif (numero >= 96 and numero <= 122):
        print("{} is lower".format(chr(numero)))
