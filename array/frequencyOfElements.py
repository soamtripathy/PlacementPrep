def frequencyOfElements(arr):
    d  = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d
x = frequencyOfElements([1, 2, 4, 3, 4, 1, 5, 3,  3, 6, 7, 5])
print(x)
