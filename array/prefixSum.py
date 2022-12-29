def prefixSum(test_list: list) -> list:
    res = [0] * len(list)
    res[0] = test_list[0]

    for i in range(1, len(test_list)):
        res[i] = res[i-1] + test_list[i]
    return("The prefix sum list is " + str(res))

list = [3, 4, 1, 7, 9, 1]
x = prefixSum(list)
print(x)

'''------------------------------------------------'''
#Using accmulate(iterable method) in Python
# function to find cumulative sum of array
from itertools import accumulate
 
def cumulativeSum(input):
    print ("Sum :", list(accumulate(input)))
 
# Driver program
if __name__ == "__main__":
    input = [4, 6, 12]
    cumulativeSum(input)