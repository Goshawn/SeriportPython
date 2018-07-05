import serial
import struct
import binascii
from time import sleep
ser = serial.Serial('COM8', baudrate = 9600)
enlem = bytes(4)

while True:

    veri = ser.read(8)
    enlemdata = veri[:4]
    boylamdata= veri[4:]
    enlem = struct.unpack('f', enlemdata)
    boylam = struct.unpack('f', boylamdata )
    print(enlem ),
    print(boylam)
