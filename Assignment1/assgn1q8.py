year = [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012]
no_application_per_year = [921261, 929198, 1043739, 1186454, 1194938, 1304495, 1356805, 1282000, 479651]

from matplotlib import pyplot as plt

plt.scatter(year, no_application_per_year)

for year_count, applicants in zip(year, no_application_per_year):
    plt.annotate("", xy=(year_count, applicants))
    
plt.title("Applicants per year")
plt.xlabel("years")
plt.ylabel("no of applicants")
plt.show()