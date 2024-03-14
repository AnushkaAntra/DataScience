salariesandtenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7),
(76000, 6), (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10), (48000, 1.9), (63000, 4.2)]

from collections import defaultdict

dict_tenure = defaultdict(list)

for i in salariesandtenures:
    dict_tenure[i[1]].append(i[0])
    
print(dict_tenure)
print()
    
dict_bucket = defaultdict(list)

for i in salariesandtenures:
    if(i[1] < 2):
        dict_bucket["less than Two"].append(i[0])
    elif(i[1] >= 2 and i[1] <= 5):
        dict_bucket["between two and five"].append(i[0])
    else:
        dict_bucket["more than five"].append(i[0])
    
print(dict_bucket)
print()

dict_avg_salaries = {}

for key in dict_bucket:
    sum = 0
    for sal in dict_bucket[key]:
        sum += sal
    avgSal = sum / len(dict_bucket[key])
    dict_avg_salaries[key] = avgSal    

print(f"Average salary for each group: {dict_avg_salaries}")