import random
from PIL import Image
import numpy as np
import colorsys
import os
import random

FULL_NAME = ""

def selectRandomFile(dir):
    return random.choice(os.listdir(dir))

def hueChange(filename, img, hue, brightness, saturation):
    # It's better to raise an exception than silently return None if img is not
    # an Image.
    r, g, b, a = img.split()
    r_data = []
    g_data = []
    b_data = []
    a_data = []

    width, heigth = img.size

    axe_pixels = ((11,4),(12,4),(12,5),(8,7),
                  (9,6),(10,7),(9,7),(8,8),
                  (9,8),(7,8),(7,9),(6,9),
                  (8,9),(6,10),(5,10),(7,10),
                  (5,11),(6,11),(4,11),(3,13),
                  (4,12),(5,12),(3,12),(2,13),
                  (4,13),(2,14),(3,14))
    
    sword_pixels = ((3,11),(4,11),(2,12),(3,12),
                    (4,12),(2,13),(3,13))

    hoe_pixels = ((9,6),(10,7),(9,7),(8,8),
                  (9,8),(7,8),(7,9),(6,9),
                  (8,9),(6,10),(5,10),(7,10),
                  (5,11),(6,11),(4,11),(3,13),
                  (4,12),(5,12),(3,12),(2,13),
                  (4,13),(2,14),(3,14),(10,6),
                  (11,6),(10,5),(12,4),(12,3),
                  (13,4),(8,7))

    pickaxe_pixels = ((9,6),(10,7),(9,7),(8,8),
                  (9,8),(7,8),(7,9),(6,9),
                  (8,9),(6,10),(5,10),(7,10),
                  (5,11),(6,11),(4,11),(3,13),
                  (4,12),(5,12),(3,12),(2,13),
                  (4,13),(2,14),(3,14),(10,6),
                  (10,5),(11,6),(12,4),(13,4),
                  (12,3),(13,3),(8,7))

    shovel_pixels = ((9,6),(10,7),(9,7),(8,8),
                     (9,8),(7,8),(7,9),(6,9),
                     (8,9),(6,10),(5,10),(7,10),
                     (5,11),(6,11),(4,11),(3,13),
                     (4,12),(3,12),(2,12),(2,13),
                     (3,13),(4,13),(5,12),(3,14),
                     (4,14),(8,7))

    sword_pixels = ((4,11),(3,13),(3,11),(2,12),
                    (4,12),(5,12),(3,12),(2,13))

    sat_avg = 0
    brg_avg = 0
    pixels = 0

    if "pickaxe" in filename:
        for x in range(width):
            for y in range(heigth):
                r,g,b,a = img.getpixel((x,y))
                if a == 255:
                    if not (x,y) in pickaxe_pixels:
                        pixels = pixels + 1
                        h,s,v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
                        sat_avg += s + saturation
                        brg_avg += v + brightness
                        rgb = colorsys.hsv_to_rgb(hue/360, max(min(s + saturation, 1), 0), max(min(v + brightness, 1), 0))
                        r, g, b = [int(x*255.) for x in rgb]
                        img.putpixel((x,y),(r,g,b))
        print("Average saturation: {} : Average brightness: {}".format(max(min((sat_avg/pixels)*100, 100), 0), max(min((sat_avg/pixels)*100, 100), 0)))
    elif "sword" in filename:
        for x in range(width):
            for y in range(heigth):
                r,g,b,a = img.getpixel((x,y))
                if a == 255:
                    if not (x,y) in sword_pixels:
                        pixels = pixels + 1
                        h,s,v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
                        sat_avg += s + saturation
                        brg_avg += v + brightness
                        rgb = colorsys.hsv_to_rgb(hue/360, max(min(s + saturation, 1), 0), max(min(v + brightness, 1), 0))
                        r, g, b = [int(x*255.) for x in rgb]
                        img.putpixel((x,y),(r,g,b))
        print("Average saturation: {} : Average brightness: {}".format(max(min((sat_avg/pixels)*100, 100), 0), max(min((sat_avg/pixels)*100, 100), 0)))
    elif "shovel" in filename:
        for x in range(width):
            for y in range(heigth):
                r,g,b,a = img.getpixel((x,y))
                if a == 255:
                    if not (x,y) in shovel_pixels:
                        pixels = pixels + 1
                        h,s,v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
                        sat_avg += s + saturation
                        brg_avg += v + brightness
                        rgb = colorsys.hsv_to_rgb(hue/360, max(min(s + saturation, 1), 0), max(min(v + brightness, 1), 0))
                        r, g, b = [int(x*255.) for x in rgb]
                        img.putpixel((x,y),(r,g,b))
        print("Average saturation: {} : Average brightness: {}".format(max(min((sat_avg/pixels)*100, 100), 0), max(min((sat_avg/pixels)*100, 100), 0)))
    elif "hoe" in filename:
        for x in range(width):
            for y in range(heigth):
                r,g,b,a = img.getpixel((x,y))
                if a == 255:
                    if not (x,y) in hoe_pixels:
                        pixels = pixels + 1
                        h,s,v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
                        sat_avg += s + saturation
                        brg_avg += v + brightness
                        rgb = colorsys.hsv_to_rgb(hue/360, max(min(s + saturation, 1), 0), max(min(v + brightness, 1), 0))
                        r, g, b = [int(x*255.) for x in rgb]
                        img.putpixel((x,y),(r,g,b))
        print("Average saturation: {} : Average brightness: {}".format(max(min((sat_avg/pixels)*100, 100), 0), max(min((sat_avg/pixels)*100, 100), 0)))
    elif "axe" in filename:
        for x in range(width):
            for y in range(heigth):
                r,g,b,a = img.getpixel((x,y))
                if a == 255:
                    if not (x,y) in axe_pixels:
                        pixels = pixels + 1
                        h,s,v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
                        sat_avg += s + saturation
                        brg_avg += v + brightness
                        rgb = colorsys.hsv_to_rgb(hue/360, max(min(s + saturation, 1), 0), max(min(v + brightness, 1), 0))
                        r, g, b = [int(x*255.) for x in rgb]
                        img.putpixel((x,y),(r,g,b))
        print("Average saturation: {} : Average brightness: {}".format(max(min((sat_avg/pixels)*100, 100), 0), max(min((sat_avg/pixels)*100, 100), 0)))
    elif "sword" in filename:
        for x in range(width):
            for y in range(heigth):
                r,g,b,a = img.getpixel((x,y))
                if a == 255:
                    if not (x,y) in sword_pixels:
                        pixels = pixels + 1
                        h,s,v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
                        sat_avg += s + saturation
                        brg_avg += v + brightness
                        rgb = colorsys.hsv_to_rgb(hue/360, max(min(s + saturation, 1), 0), max(min(v + brightness, 1), 0))
                        r, g, b = [int(x*255.) for x in rgb]
                        img.putpixel((x,y),(r,g,b))
        print("Average saturation: {} : Average brightness: {}".format(max(min((sat_avg/pixels)*100, 100), 0), max(min((sat_avg/pixels)*100, 100), 0)))
    else:
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
os.mkdir("Complete/{}".format(FULL_NAME))
os.mkdir("Complete/{}/Tools".format(FULL_NAME))
os.mkdir("Complete/{}/Element".format(FULL_NAME))
os.mkdir("Complete/{}/Block".format(FULL_NAME))

# IMAGE SETTINGS
hue = random.randint(1,360)
brightness = random.randint(-30,30)/100
saturation = random.randint(-30,30)/100

# FOREGROUND
filename = "elementOverlays/" + selectRandomFile("elementOverlays/")
basename, ext = os.path.splitext(filename)
img = Image.open(filename).convert('RGBA')
overlay_IMG = hueChange(filename, img, hue, brightness, saturation)

# BACKGROUND
filename = "elementUnderlays/" + selectRandomFile("elementUnderlays/")
underlay_IMG = Image.open(filename)
underlay_width, underlay_height = underlay_IMG.size
overlay_width, overlay_height = overlay_IMG.size
offset = (int(round((underlay_width - overlay_width) / 2)), int(round((underlay_height - overlay_height) / 2)))
underlay_IMG.paste(overlay_IMG,(0,0), overlay_IMG)
underlay_IMG.save("Complete/{}/Block/{}.png".format(FULL_NAME, FULL_NAME),"PNG")

# ELEMENT
filename = "elementItems/Elements/" + selectRandomFile("elementItems/Elements/")
basename, ext = os.path.splitext(filename)
item = Image.open(filename).convert('RGBA')
item = hueChange(filename, item, hue, brightness, saturation)
out = 'Complete/{}/Element/{}.png'.format(FULL_NAME,FULL_NAME)
item.save(out)

#TOOLS
for filename in os.listdir("elementItems/Tools/"):
    item = Image.open("elementItems/Tools/" + filename).convert('RGBA')
    item = hueChange(filename, item, hue, brightness, saturation)
    out = 'Complete/{}/Tools/{}_{}.png'.format(FULL_NAME, FULL_NAME, filename.split('.')[0])
    item.save(out)


fn.close()
sn.close()
ln.close()
