import serial
from serial import Serial
import keyboard
from time import sleep

com = serial.Serial("COM4",115200)
while True:
    dec = com.readline()
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
    elif dec == b'FF4AB5\r\n':
        break


    while True:
    if keyboard.is_pressed("-"):
        keyboard.press("4")
        sleep(0.2)
    if keyboard.is_pressed("i"):
        sleep(0.2)
        break
print("Hello World!")