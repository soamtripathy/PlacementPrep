def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num%i == 0):
                return False
                break
        else:
            return True
x = prime(29)
print(x)
