def swap(i, min, a):
    temp = a[i]
    a[i] = a[min]
    a[min] = temp
    return a

# Bubble Sort
a = [6, 3, 5, 1, 2, 0, 4, 8, 7, 9]
for i in range(0, len(a) - 1):
    for j in range(0, len(a) - 1 - i):
        if a[j+1] < a[j]:
            a = swap(j, j+1, a)
print(a)
