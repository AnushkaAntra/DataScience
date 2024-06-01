users=[
    {'id':0,'name':'Ashok'},
    {'id':1, 'name':'Rahul'},
    {'id':2, 'name':'Sarita'},
    {'id':3, 'name':'Rohan'},
    {'id':4, 'name':'Akhaya'},
    {'id':5, 'name':'Prakash'},
    {'id':6, 'name':'Madhabi'},
    {'id':7, 'name':'Spandan'}
   
    ]

interests=[(0,'python'),(0,'java'),(1,'java'),(2,'python'),(2,'java'),(3,'python'),(4,'c'),(5,'c'),
           (6,'python'),(7,'java')]

#1
def who_like(target_interest):
    return [user_id for user_id, interest in interests if(interest == target_interest)]

print(who_like('python'))

#2
from collections import defaultdict

user_id_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_id_by_interest[interest].append(user_id)

print(user_id_by_interest)

#3
interest_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interest_by_user_id[user_id].append(interest)
    
print(interest_by_user_id)

#4
from collections import Counter

def most_common_interest(user):
    user_id = user['id']
    return Counter(x 
                   for interest in interest_by_user_id[user_id] 
                   for x in interest_by_user_id[interest] 
                   if(user_id != x))

print(most_common_interest(users[1]))
    