
n = int(input("enter the no of string want to enter: "))
StringList = []
for i in range(0, n):
    string = input("enter an string: ")
    StringList.append(string)

print(StringList)

from collections import Counter

no_of_items = dict(Counter(StringList))
print(no_of_items)

MStringList = []
for key, val in no_of_items.items():
    if(val >= 2):
        MStringList.append(key)
        
print(MStringList)

for i in MStringList:
    if(no_of_items[i]%2 == 0):
        print(f"{i} occur even no of times")
    else:
        print(f"{i} occur odd no of times")
        
def remove_string(string, pos):
    count = 0
    for index in range(len(StringList)):
        i=StringList[index]
        if(string == i):
            count+=1
            if(count==pos):
                print(index)
                StringList.pop(index)
                break
        
remove_string("anushka", 2)
print(StringList)