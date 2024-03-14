from matplotlib import pyplot as plt

string = input("enter the string: ")

from collections import Counter

freq = dict(Counter(string.lower()))
print(freq)

plt.bar(freq.keys(), freq.values(), color="lightpink")
plt.title("frequency of alphabets")
plt.xlabel("alphabets")
plt.ylabel("frequency")
plt.show()
