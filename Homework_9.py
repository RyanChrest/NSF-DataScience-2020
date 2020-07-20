# Perform a linear regression on each data set in AnscombesQuartet.csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load in csv as a data frame
data = pd.read_csv("../AnscombesQuartet.csv")

# Create figure for subplots
fig, ax = plt.subplots(nrows=2,ncols=2)
fig.set_size_inches(12,8)

# Perform linear regression on x1 and y1
x1 = np.array(data['x1'])
y1 = np.array(data['y1'])

slope1, intercept1, r_value1, p_value1, std_err1 = linregress(x1,y1)

ax[0,0].scatter(x1,y1)
ax[0,0].plot(x1, intercept1 + slope1*x1, color="red")
ax[0,0].set_xlim(3, 20)
ax[0,0].set_ylim(3, 15)
ax[0,0].set_title('Set 1')

# Perform linear regression on x2 and y2
x2 = np.array(data['x2'])
y2 = np.array(data['y2'])

slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x2,y2)

ax[0,1].scatter(x2,y2)
ax[0,1].plot(x2,intercept2 + slope2*x2, color="red")
ax[0,1].set_xlim(3, 20)
ax[0,1].set_ylim(3, 15)
ax[0,1].set_title('Set 2')

# Perform linear regression on x3 and y3
x3 = np.array(data['x3'])
y3 = np.array(data['y3'])

slope3, intercept3, r_value3, p_value3, std_err3 = linregress(x3,y3)

ax[1,0].scatter(x3,y3)
ax[1,0].plot(x3, intercept3 + slope3*x3, color="red")
ax[1,0].set_xlim(3, 20)
ax[1,0].set_ylim(3, 15)
ax[1,0].set_title('Set 3')

# Perform linear regression on x3 and y3
x4 = np.array(data['x4'])
y4 = np.array(data['y4'])

slope4, intercept4, r_value4, p_value4, std_err4 = linregress(x4,y4)

ax[1,1].scatter(x4,y4)
ax[1,1].plot(x4, intercept4 + slope4*x4, color="red")
ax[1,1].set_xlim(3, 20)
ax[1,1].set_ylim(3, 15)
ax[1,1].set_title('Set 4')

# Show plot
plt.show()
