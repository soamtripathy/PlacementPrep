def powerOfNum(num, power):
    if power == 0:
        return 1
    else:
        return num*powerOfNum(num, power-1)

print(powerOfNum(2, 5))