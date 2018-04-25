# HackerRank Laptop Battery Challenge

import StringIO
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt

#full csv data
#'col1,col2\n2.81,5.62\n7.14,8.00\n2.72,5.44\n3.87,7.74\n1.90,3.80\n7.82,8.00\n7.02,8.00\n5.50,8.00\n9.15,8.00\n4.87,8.00\n8.08,8.00\n5.58,8.00\n9.13,8.00\n0.14,0.28\n2.00,4.00\n5.47,8.00\n0.80,1.60\n4.37,8.00\n5.31,8.00\n0.00,0.00\n1.78,3.56\n3.45,6.90\n6.13,8.00\n3.53,7.06\n4.61,8.00\n1.76,3.52\n6.39,8.00\n0.02,0.04\n9.69,8.00\n5.33,8.00\n6.37,8.00\n5.55,8.00\n7.80,8.00\n2.06,4.12\n7.79,8.00\n2.24,4.48\n9.71,8.00\n1.11,2.22\n8.38,8.00\n2.33,4.66\n1.83,3.66\n5.94,8.00\n9.20,8.00\n1.14,2.28\n4.15,8.00\n8.43,8.00\n5.68,8.00\n8.21,8.00\n1.75,3.50\n2.16,4.32\n4.93,8.00\n5.75,8.00\n1.26,2.52\n3.97,7.94\n4.39,8.00\n7.53,8.00\n1.98,3.96\n1.66,3.32\n2.04,4.08\n11.72,8.00\n4.64,8.00\n4.71,8.00\n3.77,7.54\n9.33,8.00\n1.83,3.66\n2.15,4.30\n1.58,3.16\n9.29,8.00\n1.27,2.54\n8.49,8.00\n5.39,8.00\n3.47,6.94\n6.48,8.00\n4.11,8.00\n1.85,3.70\n8.79,8.00\n0.13,0.26\n1.44,2.88\n5.96,8.00\n3.42,6.84\n1.89,3.78\n1.98,3.96\n5.26,8.00\n0.39,0.78\n6.05,8.00\n1.99,3.98\n1.58,3.16\n3.99,7.98\n4.35,8.00\n6.71,8.00\n2.58,5.16\n7.37,8.00\n5.77,8.00\n3.97,7.94\n3.65,7.30\n4.38,8.00\n8.06,8.00\n8.05,8.00\n1.10,2.20\n6.65,8.00'

#csv data after dropping the outliers picked from the scatter plot
data = 'col1,col2\n2.81,5.62\n2.72,5.44\n3.87,7.74\n1.90,3.80\n0.14,0.28\n0.80,1.60\n0.00,0.00\n1.78,3.56\n3.45,6.90\n3.53,7.06\n1.76,3.52\n0.02,0.04\n2.06,4.12\n2.24,4.48\n1.11,2.22\n2.33,4.66\n1.83,3.66\n1.14,2.28\n1.75,3.50\n2.16,4.32\n1.26,2.52\n3.97,7.94\n1.98,3.96\n1.66,3.32\n2.04,4.08\n3.77,7.54\n1.83,3.66\n2.15,4.30\n1.58,3.16\n1.27,2.54\n3.47,6.94\n1.85,3.70\n0.13,0.26\n1.44,2.88\n3.42,6.84\n1.89,3.78\n1.98,3.96\n0.39,0.78\n1.99,3.98\n1.58,3.16\n3.99,7.98\n2.58,5.16\n3.97,7.94\n3.65,7.30\n1.10,2.20'

#reading a CSV file from StringIO into a pandas DataFrame
df = pd.read_csv(StringIO.StringIO(data)) 

#visualize data to eliminate outliers and discover boundary conditions
plt.clf
df.plot(kind="scatter", x="col1", y="col2", alpha=0.5)
#display()

x_train = df['col1'].reshape(-1,1)
y_train = df['col2'].reshape(-1,1)

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train) 

#replace integer 4 with sys.stdin.read().strip() to take a stdin input
timeCharged = float(2.3)
timeCharged_arr = np.array([timeCharged]).reshape(1,-1)

prediction = lin_reg.predict(timeCharged_arr)

if timeCharged > 4.00: sys.stdout.write(str(float(8)))
else: sys.stdout.write(str(prediction[0,0])) 
