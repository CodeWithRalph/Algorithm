def swap(i, min, a):
    temp = a[i]
    a[i] = a[min]
    a[min] = temp
    return a

# Insertion Sort
a = [6, 3, 5, 1, 2, 0, 4, 8, 7, 9]
for i in range(0, len(a) - 1):
    min = i
    for j in range(i + 1, len(a)):
        if a[j] < a[min]:
            min = j
    a = swap(i, min, a)
print(a)
