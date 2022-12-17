def countNumber(num):
    count = 0
    while (num!= 0):
        num = num // 10
        count += 1
    return count
x = countNumber(17689)
print(x)
