#This is a Leetcode question(136.Single Number)
#This is solved using XOR operation.
def singleNumber(arr):
    uniNum = 0
    for i in arr:
        uniNum = uniNum ^ i
    return uniNum
x = singleNumber([4,1,2,1,2])
print(x)