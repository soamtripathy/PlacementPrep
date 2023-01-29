#Parameterised
# def sumOfN(i, sum):
#     if i < 1:
#         print(sum)
#         return
#     sumOfN(i-1, sum+i)
# sumOfN(10, 0)
#functionally
def sumOfN(n):
    if n == 0:
        return 0
    return n + sumOfN(n-1)
print(sumOfN(5))
    