test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

from matplotlib import pyplot as plt

plt.scatter(test_1_grades, test_2_grades)
plt.title("Unequal axis")
plt.xlabel("Test 1 grade")
plt.ylabel("Test 2 grade")
plt.show()

plt.scatter(test_1_grades, test_2_grades)
plt.title("Equal axis")
plt.xlabel("Test 1 grade")
plt.ylabel("Test 2 grade")
plt.axis("equal")
plt.show()