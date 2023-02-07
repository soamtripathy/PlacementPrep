from collections import Counter
def stabilizer(arr, N):
    d = Counter(arr)
    l1 = []
    for i in arr:
        l1.append(N-d[i])
    return l1

print(stabilizer([15, 16, 22, 45, 75], 6))