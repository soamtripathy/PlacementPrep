#Trying in built function of python using math module
import math;
def factorial(num):
    fact = math.factorial(num)
    return fact
x = factorial(5)
print(x)
#trying with another menthod
def factorial(num):
    ans = 1
    for i in range(1, num+1):
        ans *= i
    return ans
x = factorial(5)
print(x)
