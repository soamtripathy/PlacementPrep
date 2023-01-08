def thirdMax(nums) :
    nums = sorted(list(set(nums)))
    if len(nums) > 2:
        return nums[-3]
    return nums[-1]
print(thirdMax([2,2,3,1]))
