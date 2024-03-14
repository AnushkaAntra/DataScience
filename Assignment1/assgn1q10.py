male_age = [53,51,71,31,33,39,52,27,54,30,64,26,21,54,52,20,59,32]
female_age = [53,65,68,21,75,46,24,63,61,24,49,41,39,40,25,54,42, 32,48,23,23]

from collections import Counter
from matplotlib import pyplot as plt

histogram1 = Counter(min(m_age // 10*10, 90) for m_age in male_age)

plt.bar([x for x in histogram1.keys()],histogram1.values(), 10, edgecolor=(0,0,0))

plt.axis([0,80, 0, 8])

plt.xticks([10*i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of males")
plt.title("Distribution of Male ages")
plt.show()

histogram2 = Counter(min(f_age // 10*10, 90) for f_age in female_age)

plt.bar([x for x in histogram2.keys()],histogram2.values(), 10, color="pink", edgecolor=(0,0,0))

plt.axis([0,80, 0, 8])

plt.xticks([10*i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of females")
plt.title("Distribution of Female ages")
plt.show()