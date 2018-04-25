# Creating shapes in numpy
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
x, y = np.indices((80, 80))
x1, y1, x2, y2 = 28, 28, 44, 52
r1, r2 = 16, 20
mask_circle1 = (x - x1) ** 2 + (y - y1) ** 2 < r1 ** 2
mask_circle2 = (x - x2) ** 2 + (y - y2) ** 2 < r2 ** 2
image = np.logical_or(mask_circle1, mask_circle2)
distance_map = ndimage.distance_transform_edt(image)
plt.imshow(distance_map) 
display()

# Create a chess board in numpy
import numpy as np
import matplotlib.pyplot as plt
check = np.zeros((1000, 1000))
check[::2, 1::2] = 1
check[1::2, ::2] = 1
plt.imshow(check, cmap='gray', interpolation='nearest') 
display()

# Plotting a dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = np.array([[1,2,100000,40000],
              [2,2,10000,10000],
              [3,3,30000,80000]])
#x=np.arange(9)
#x[:,8]
x.shape
df = pd.DataFrame(x,
                 index = list(range(0,3)),
                 columns = list('abcd'))
df.plot(kind='scatter',
       x='a',
       y='b',
       alpha=0.5,
       s=df['c']/100,
       label='c',
       c='d',
       cmap=plt.get_cmap('jet'),
       colorbar=True)
plt.legend()
plt.show()
display()
