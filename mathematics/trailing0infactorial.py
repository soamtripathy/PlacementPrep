#Problem Description
#Let we have to find the ending zero or trailing zero of a factorial.
#In the first step, we have to find the factorial of the number given.
#Use while loop to count the avilable zero
#Divide the factorial by 10, If there is no remainder available, move to the next line by dividing factorial with 10
#and increase the count by 1
#do this untill the desired result is out
import math;
def countTrailingZero(num):
    fact = math.factorial(num)
    count = 0
    while (fact % 10 == 0):
        fact = fact // 10
        count += 1
    return count
x = countTrailingZero(50)
print(x) 