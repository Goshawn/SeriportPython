from ast import literal_eval
from time import sleep
import serial
import struct
import string
import time
import binascii
ser = serial.Serial('COM11', 9600)
enlem = bytes(4)



while True:

    veri = ser.read(8)
    data= [ord(i) for i in veri]
    enlemdata = data[:4]
    boylamdata= data[4:]
    varan1 = binascii.hexlify(bytearray(enlemdata))
    enlem = struct.unpack('f', varan1.decode('hex'))[0]
    varan2 = binascii.hexlify(bytearray(boylamdata))
    boylam = struct.unpack('f', varan2.decode('hex'))[0]
    print(enlem)
    print(boylam)


