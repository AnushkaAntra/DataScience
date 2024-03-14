mentions = [500, 505]
years = [2017, 2018]

from matplotlib import pyplot as plt

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times")
plt.ticklabel_format(useOffset=False)
plt.axis([2016.5, 2018.5, 499, 506])
plt.show()


plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times")
plt.ticklabel_format(useOffset=False)
plt.axis([2017, 2018, 499, 506])
plt.show()