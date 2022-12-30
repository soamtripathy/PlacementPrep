def secondMax(arr):
    max1 =  arr[0]
    max2 = arr[0]
    for i in range(1, len(arr)):
        if max1 <= arr[i]:
            max2 = max1
            max1 = arr[i]
        elif max2 < arr[i]:
            max2 = arr[i]
    return max2

x = secondMax([1, 5, -3, -4, 7, 9, 6])
print(x)
