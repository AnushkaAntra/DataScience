def median(l : list) -> float:
    n = len(l)
    l = sorted(l)
    if(n%2 != 0):
        return l[n//2]
    else:
        return (l[(n-1)//2] + l[n//2])/2
    
l = eval(input("enter the list: "))
print("median is:",median(l))
        