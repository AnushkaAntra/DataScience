max = [17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18]
min = [-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58]

from matplotlib import pyplot as plt

xs = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

plt.plot(xs, max, 'r-', label = "Max")
plt.plot(xs, min, 'b-', label = "Min")

plt.legend()
plt.xlabel("Months")
plt.ylabel("Temp (in degree celcius)")
plt.show()



