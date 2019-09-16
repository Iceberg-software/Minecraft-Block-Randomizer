import random
from PIL import Image
import numpy as np

FULL_NAME = ""

def colorMask(im):
    im = im.convert('RGBA')

    for i, pixel in enumerate()

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

ore = Image.open('Images/ore.png')
colorMask(ore)

fn.close()
sn.close()
ln.close()
