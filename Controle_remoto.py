import serial
from serial import Serial
import keyboard
from time import sleep

com = serial.Serial("COM3",9600)

while True:
    dec = com.readline()
    cod = dec.decode("ascii")
    print(dec)
    if dec == b'FFC23D\r\n':
        keyboard.press("space") 
    elif dec == b'FF22DD\r\n':
        keyboard.press("left")
    elif dec == b'FF02FD\r\n':
        keyboard.press("right")
    elif dec == b'FFA857\r\n':
        keyboard.press("up")
    elif dec == b'FFE01F\r\n':
        keyboard.press("down")
    elif dec == b'FF42BD\r\n':
        keyboard.press("i")
    elif dec == b'FF6897\r\n':
        keyboard.press("tab")
    elif dec == b'FF906F\r\n':
        keyboard.press("enter")
    elif dec == b'FF52AD\r\n':
        keyboard.press("f")
