# create Mandelbrot set 
# Loading in relevant packages
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.patches as patches
#from scipy.misc import imread
#import base64
#import codecs
#import cv2 #Used for converting the coastline images to grayscale
#from scipy import misc
#%matplotlib inline 
def mandelbrot(n, m, itermax, xmin, xmax, ymin, ymax):
    ix, iy = np.mgrid[0:n, 0:m]
    x = np.linspace(xmin, xmax, n)[ix]
    y = np.linspace(ymin, ymax, m)[iy]
    c = x+complex(0,1)*y
    del x, y
    img = np.zeros(c.shape, dtype=int)
    ix.shape = n*m
    iy.shape = n*m
    c.shape = n*m
    z = np.copy(c)
    for i in range(itermax):
        if not len(z): break
        np.multiply(z, z, z)
        np.add(z, c, z)
        rem = abs(z)>2.0
        img[ix[rem], iy[rem]] = i+1
        rem = ~rem
        z = z[rem]
        ix, iy = ix[rem], iy[rem]
        c = c[rem]
    return img

plt.figure(figsize=(15,10))

import time
start = time.time()
I = mandelbrot(400, 400, 100, -2, .5, -1.25, 1.25)
print('Running time:', time.time()-start)
I[I==0] = 101
img = plt.imshow(I.T, origin='lower left', cmap='afmhot')
axes = plt.gca()
# Hide grid lines
axes.grid(False)
# Hide axes ticks
axes.set_xticks([])
axes.set_yticks([])
plt.show()
display()
