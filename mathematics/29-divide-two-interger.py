def divide(dividend, divisor) :
    store= int(dividend/divisor)
    limit = 2**31
    limit1 = limit-1
    if store>limit1:
        return limit1
    limit2 = -limit
    if store<limit2:
        return limit2
    return store
print(divide(10, 3))
print(divide(7, 3))