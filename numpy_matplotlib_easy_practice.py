from matplotlib import pyplot as plt
import numpy as np
from numpy import linspace

x = linspace(0, 1.5, num=1000)

y1 = x
y2 = x ** 2

plt.plot(x, y1)
plt.plot(x, y2)


plt.show()


