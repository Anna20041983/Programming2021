# Program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes
# Author: Anna Kozakiewicz

import numpy as np
import matplotlib.pyplot as plt

# change background color to black 
plt.style.use('dark_background')

xpoints = np.array (range(0, 4))
gpoints = xpoints * xpoints
hpoints = xpoints * xpoints * xpoints

plt.plot (xpoints, xpoints, label = 'straight', color='yellow') 
plt.plot (xpoints, gpoints, label = 'xsquared', color = 'orange')
plt.plot (xpoints, hpoints, label = 'xcubed', color = 'red')

plt.legend()
plt.show()
