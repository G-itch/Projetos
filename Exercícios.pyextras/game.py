from ppadb.client import Client
from PIL import Image
import numpy
adb = Client(host ="127.0.0.1", port= 5037)

devices = adb.devices()

if len(devices) == 0:
    print("none")
    print(1)
    quit()

device = devices[0]

image = device.screencap()

with open("joguin/im.jpg","wb") as img:
    img.write(image)
# device.shell("input touchscreen swipe 500 500 500 500 2000")
image = Image.open("joguin/im.jpg",)

image = numpy.array(image,dtype=numpy.uint8)

pixels = [list(i[:3]) for i in image[913]]
transitions = []
ignore = True
black = True

for i, pixel in enumerate(pixels):
    r,g,b = [int(i) for i in pixel]
    # print(r,g,b,i)
    """if r == 247 and g == 27 and b==27:
        print(r,g,b,i)
        reds.append(i)"""
    if ignore and (r+g+b) != 0:
        continue
    
    ignore = False
    
    if black and (r+g+b) != 0:
        black = not black
        transitions.append(i)
        continue
    
    if not black and (r+g+b) == 0:
        black = not black
        transitions.append(i)
        continue    
    
    if not black and r+g+b == 0:
        black = not black
        transitions.append(i)
start, target1, target2 = transitions[0],transitions[1],transitions[2]
gap = target1 - start
target = target2 - target1
distance = (gap + target / 2) * .98

print(f'transition points: {transitions}, distance: {distance}')

device.shell(f'input touchscreen swipe 500 500 500 500 {int(distance)+200}')

        
print(transitions)
# device.shell("input touchscreen swipe 500 500 500 500 {}".format(int(reds[7]-(transitions[0]/2)+50)))