from typing import List
matrix = List[List[float]]

def create_matrix(m : int, n : int) -> matrix:
    return [[i+j for j in range(n)] for i in range(m)]

m = int(input("enter the no of rows: "))
n = int(input("enter the no of cols: "))
print(create_matrix(m, n))
