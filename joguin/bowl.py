from ppadb.client import Client
import time
adb = Client(host ="127.0.0.1", port= 5037)

devices = adb.devices()

if len(devices) == 0:
    print("none")
    print(1)
    quit()

device = devices[0]
device.shell('input touchscreen swipe 640 900 619 900 400')
time.sleep(0.3)
device.shell('input touchscreen swipe 640 900 640 590 500')