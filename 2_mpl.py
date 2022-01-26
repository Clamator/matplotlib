import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator, MultipleLocator, MaxNLocator

fig = plt.figure(figsize=(5, 5))  # window
ax = fig.add_subplot(1, 1, 1)  # coordinate system
#ax2 = fig.add_subplot(1, 2, 2)
lines1 = ax.plot([1, 5, 1, 5], [1, 5, 5, 1])  # graph1
lines2 = ax.plot([2, 4, 1, 2], [3, 7, 6, 10])  # graph2
ax.set(xlim=(-2, 10))
ax.set_ylim(ymin=-2, ymax=10)

# lc = NullLocator() # оставляет только по одной выбранной стороне линии
ax.grid()
# ax.xaxis.set_major_locator(lc)
ax.xaxis.set_major_locator(MultipleLocator(base=1))
ax.yaxis.set_major_locator(MultipleLocator(base=1))
#ax.yaxis.set_major_locator(MaxNLocator(16))

plt.show()
