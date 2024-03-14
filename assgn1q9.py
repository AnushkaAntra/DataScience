import math
from matplotlib import pyplot as plt

def sine(x):
    return math.sin(x)

x_values = []
for i in range(-10, 10):
    x_values.append(i)
    

#(i)
y_values1 = []
for x in x_values:
    y_values1.append(x*sine(x))

#(ii)
y_values2 = []
for x in x_values:
    y_values2.append(math.pow(x,2)*sine(x))

#(iii)
y_values3 = []
for x in x_values:
    y_values3.append(math.pow(x,3)*sine(x))

#(iv)
y_values4 = []
for x in x_values:
    y_values4.append(math.pow(x,4)*sine(x))

plt.plot(x_values, y_values1, 'r-', label = "xsinx")
plt.plot(x_values, y_values2, 'g-', label = "x2sinx")
plt.plot(x_values, y_values3, 'b-', label = "x3sinx")
plt.plot(x_values, y_values4, 'y-', label = "x4sinx")


plt.legend(loc = 9)
plt.xlabel("X-axis")
plt.title("Sine Graph")
plt.show()
