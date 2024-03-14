salaries_and_tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7),
(76000, 6), (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10),
(48000, 1.9), (63000, 4.2)]

from collections import defaultdict

def predict_paid_or_unpaid(years_experience):
    if(years_experience < 3.0 or years_experience > 8.0):
        return "paid"
    else:
        return "unpaid"
    
salary_per_tenure = defaultdict(str)

for i in salaries_and_tenures:
    salary_per_tenure[i[1]] = predict_paid_or_unpaid(i[1])
    
print(salary_per_tenure)