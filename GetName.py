import random
from PIL import Image
import numpy as np
import colorsys
import os
import random

FULL_NAME = ""

def selectRandomFile(dir):
    return random.choice(os.listdir(dir))

def hueChange(img, hue, brightness, saturation):
    # It's better to raise an exception than silently return None if img is not
    # an Image.
    img.load()
    r, g, b, a = img.split()
    r_data = []
    g_data = []
    b_data = []
    a_data = []

    width, heigth = img.size

    sat_avg = 0
    brg_avg = 0
    pixels = 0

    for x in range(width):
        for y in range(heigth):
            r,g,b,a = img.getpixel((x,y))
            if a == 255:
                pixels = pixels + 1
                h,s,v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
                sat_avg += s + saturation
                brg_avg += v + brightness
                rgb = colorsys.hsv_to_rgb(hue/360, max(min(s + saturation, 1), 0), max(min(v + brightness, 1), 0))
                r, g, b = [int(x*255.) for x in rgb]
                img.putpixel((x,y),(r,g,b))
    print("Average saturation: {} : Average brightness: {}".format(max(min((sat_avg/pixels)*100, 100), 0), max(min((sat_avg/pixels)*100, 100), 0)))

    return(img)

    #for rd, gr, bl, al in zip(r.getdata(), g.getdata(), b.getdata(), a.getdata()):
    #    if al == 255:
    #        h, s, v = colorsys.rgb_to_hsv(rd / 255., bl / 255., gr / 255.) 
    #        rgb = colorsys.hsv_to_rgb(hue/360., s, v)
    #        rd, gr, bl = [int(x*255.) for x in rgb]
    #        r_data.append(rd)
    #        g_data.append(gr)
    #        b_data.append(bl)

    #r.putdata(r_data)
    #g.putdata(g_data)
    #b.putdata(b_data)


def fileLen(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i-1

fn = open("firstNames.txt")
sn = open("secondNames.txt")
ln = open("lastNames.txt")

firstNames = fn.readlines()
secondNames = sn.readlines()
lastNames = ln.readlines()

fn.close()
sn.close()
ln.close()

firstName = random.randint(0,1)
fourthName = random.randint(0,1)
fifthName = random.randint(0,1)
sixthName = random.randint(0,1)

if firstName == 1:
    FULL_NAME += firstNames[random.randint(0,fileLen("firstNames.txt"))].replace("\n", "")

FULL_NAME += secondNames[random.randint(0,fileLen("secondNames.txt"))].replace("\n", "")
FULL_NAME += firstNames[random.randint(0,fileLen("firstNames.txt"))].replace("\n", "")

if fourthName == 1:
    FULL_NAME += secondNames[random.randint(0,fileLen("secondNames.txt"))].replace("\n", "")

if fifthName == 1:
    FULL_NAME += firstNames[random.randint(0,fileLen("firstNames.txt"))].replace("\n", "")

if sixthName == 1:
    FULL_NAME += lastNames[random.randint(0,fileLen("lastNames.txt"))].replace("\n", "")

print("")
print(FULL_NAME)

#FOREGROUND

filename = 'elementOverlays/HUE/ore.png'
basename, ext = os.path.splitext(filename)
img = Image.open(filename).convert('RGBA')
hue = 125
brightness = 0
saturation = -100/100
overlay_IMG = hueChange(img, hue, brightness, saturation)
out = '{}_hue{:03d}.png'.format(basename,hue)
overlay_IMG.save(out)

# BACKGROUND

filename = selectRandomFile("elementUnderlays/")
underlay_IMG = Image.open("elementUnderlays/" + filename)
underlay_width, underlay_height = underlay_IMG.size
overlay_width, overlay_height = overlay_IMG.size
offset = (int(round((underlay_width - overlay_width) / 2)), int(round((underlay_height - overlay_height) / 2)))
underlay_IMG.paste(overlay_IMG, offset)
underlay_IMG.save("PURE_ELEMENT.png")

fn.close()
sn.close()
ln.close()
