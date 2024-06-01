interests=[(0,'Hadoop'),(1,'c'),(1,'c++'), (2,'java'),(2,'Data Science'),(2,'Big Data'), 
           (3,'python'),(3,'data mining'),(4,'web mining'),(4,'data structure'),
           (5,'deep learning'),(5,'machine learning'),(6, 'java')] 

#1
from collections import defaultdict

user_id_by_interests = defaultdict(list)

for user_id, interest in interests:
    user_id_by_interests[interest].append(user_id)
    
no_of_user_by_interest = [(interest, len(user)) for interest, user in user_id_by_interests.items()]

    
print("the popular interest is:", max(no_of_user_by_interest, key = lambda x : x[1]))