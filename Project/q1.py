users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" },  
]
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

#1

freindships = {user['id'] : [] for user in users}

for i, j in friendship_pairs:
    freindships[i].append(j)
    freindships[j].append(i)
    
print(freindships)

#2

def number_of_friends(user):
    user_id = user['id']
    freinds = freindships[user_id]
    return len(freinds)

total_connections = sum(number_of_friends(user) for user in users)

avg_connections = total_connections/len(users)

print("total connections is:", total_connections, "and average connections is:",avg_connections)

#3

number_of_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

number_of_friends_by_id.sort(key = lambda x : x[1], reverse = True)

print(number_of_friends_by_id)

#4

from collections import Counter

def friend_of_friends(user):
    user_id = user['id']
    return Counter(x 
                   for friend_id in freindships[user_id] 
                   for x in freindships[friend_id] 
                   if user_id != x 
                   and x not in freindships[user_id])

print(friend_of_friends(users[3]))