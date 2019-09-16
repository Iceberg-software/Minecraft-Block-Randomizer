from skimage import data, color, img_as_float
import numpy as np
import matplotlib.pyplot as plt 

def tint():
    gray_image = img_as_float(data.camera())
    image = color.gray2rgb(gray_image)

    overlay = [1,1,0]

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4), sharex=True, sharey=True)
    ax1.imshow(overlay*image)

tint()