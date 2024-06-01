salaries_and_tenures = [(83000, 8), (88000, 8),(48000, 1), (76000, 6),(69000, 6), (76000, 7), 
                        (60000, 2), (83000, 10),(48000, 2), (63000, 4), (52000,1),(85000,8),
                        (71000,5),(80000,7)]

#1
from collections import defaultdict

salaries_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salaries_by_tenure[tenure].append(salary)
    
print(salaries_by_tenure)

tenure_avg_salary = { tenure : sum(salaries)/len(salaries) for tenure, salaries in salaries_by_tenure.items() }

print(tenure_avg_salary)

#2

buckets_of_tenures = defaultdict(list)

for salary,tenure in salaries_and_tenures:
    if(tenure < 2):
        buckets_of_tenures["less than 2"].append(salary)
    elif(2<=tenure<=5):
        buckets_of_tenures["Between 2 and 5"].append(salary)
    else:
        buckets_of_tenures["more than 5"].append(salary)
        
print(buckets_of_tenures)

#3

bucket_avg_salary = { tenure : sum(salaries)/len(salaries) for tenure, salaries in buckets_of_tenures.items()}

print(bucket_avg_salary)