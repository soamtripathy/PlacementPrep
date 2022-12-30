def maxElement(arr):
    res = arr[0]
    for i in arr:
        if i > res:
            res = i

    return res
x  = maxElement([3, 1, 3, 5, 6, 2])
print(x)
'''-------------------------------------------------'''
#Using max in python
def maxElement(arr):
    return max(arr)
x  = maxElement([3, 1, 3, 5, 6, 2])
print(x)