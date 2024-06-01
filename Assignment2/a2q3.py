from typing import List
matrix = List[List[float]]
vector = List[float]

def extract_row(m : matrix, i : int) -> vector:
    return m[i-1]

def extract_col(m : matrix, j : int) -> vector:
    return [m[i][j-1] for i in range(len(m))]

def main():
    n = int(input("Enter the row no: "))
    mat = eval(input("Enter the matrix: "))
    print(f"Row {n} is: {extract_row(mat, n)}")
    print(f"Column {n} is: {extract_col(mat, n)}")
    
main()