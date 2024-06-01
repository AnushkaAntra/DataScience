from typing import List
Vector = List[float]

def vectors_mean(vectors : List[Vector]) -> Vector:
    numElements = len(vectors[0])
    n = len(vectors)
    assert all(len(vector) == numElements for vector in vectors), "Length of vectors are different"
    return [(1/n)*ele for ele in [sum(vector[i] for vector in vectors) for i in range(numElements)]]

l = eval(input("enter the list of vectors"))
print("component wise mean of the vectors:",vectors_mean(l))