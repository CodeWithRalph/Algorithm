# Quick Sort
a = [4, 3, 7, 6, 1, 5, 8, 2]

def quickSort(inputArray):
    if len(inputArray) < 2:
        return inputArray
    pivotPoint = inputArray[-1]
    L = []
    E = []
    G = []
    E += [pivotPoint]
    for element in inputArray[:-1]:
        if element == pivotPoint:
            E += [element]
        elif element < pivotPoint:
            L += [element]
        else:
            G += [element]
    if len(L) > 1:
        L = quickSort(L)
    if len(E) > 1:
        E = quickSort(E)
    if len(G) > 1:
        G = quickSort(G)
    return L + E + G
    
a = quickSort(a)
print(a)