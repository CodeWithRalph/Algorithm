a = [3, 13, 27, 31, 39, 42, 55, 70, 74, 81, 85, 93, 98]
l = 0
r = len(a)
key = 70
mid = len(a)//2
while (l != r):
    if a[mid] < key:
        l = mid + 1
    else:
        r = mid
    mid = () // 2
print(l)
