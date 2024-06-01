from typing import List
vector = List[float]

def addition(v : vector, w : vector) -> vector:
    if(len(v) == len(w)):
        return [vi+wi for vi, wi in zip(v,w)]

def subtraction(v : vector, w : vector) -> vector:
    if(len(v) == len(w)):
        return [vi-wi for vi, wi in zip(v, w)]

def scalar_multiply(n : int, v : vector) -> vector:
    return [n*vi for vi in v]

def dot_product(v : vector, w : vector) -> float:
    if(len(v) == len(w)):
        return sum(vi*wi for vi, wi in zip(v, w))

def length(v : vector) -> int:
    return len(v)
        
def main():
    print("0 : exit")
    print("1 : addition")
    print("2 : subtraction")
    print("3 : scalar multiply")
    print("4 : Dot product")
    print("5 : length of vector")
    
    n = int(input("enter the choice"))
    while(n != 0):
        if(n == 1):
            l1 = eval(input("enter the list1"))
            l2 = eval(input("enter the list2"))
            print(addition(l1, l2))
        elif(n == 2):
            l1 = eval(input("enter the list1"))
            l2 = eval(input("enter the list2"))
            print(subtraction(l1, l2))
        elif(n == 3):
            x = int(input("enter the number:"))
            l1 = eval(input("enter the list:"))
            print(scalar_multiply(x, l1))
        elif(n == 4):
            l1 = eval(input("enter the list1"))
            l2 = eval(input("enter the list2"))
            print(dot_product(l1, l2))
        elif(n == 5):
            l1 = eval(input("enter the list"))
            print(length(l1))
        else:
            print("enter the valid choice")
        n = int(input("enter the choice"))
    if(n == 0):
        return
        
main()
        