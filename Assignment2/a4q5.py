#from collections import Counter
import random
from matplotlib import pyplot as plt

integers = [random.randint(1,100) for i in range(100)]

plt.hist(integers, bins=20, color = 'lightgreen', edgecolor = 'black')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Random Integers")
plt.show()