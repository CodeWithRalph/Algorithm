# Selection sort

a = [4, 3, 7, 9, 6, 1, 5, 8, 10, 2]

for i in range(1, len(a)):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = key
print(a)
