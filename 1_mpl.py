import numpy
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 5, 5, 1, 1])
y = np.array([1, 1, 5, 5, 1])

x2 = [1, 5, 1, 5]
y2 = [1, 5, 5, 1]

plt.plot(x, y, '--', marker='D', markerfacecolor='r', linewidth='4')
plt.plot(x2, y2, ':o')
plt.title('food')
plt.ylabel('wastes')
plt.legend('food-1')
plt.xlabel('day')
plt.show()