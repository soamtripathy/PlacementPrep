def smallerNumbersThanCurrent(nums):
    arr = sorted(nums)
        
    for i in range(len(nums)):
        nums[i] = arr.index(nums[i])
        
    return nums
print(smallerNumbersThanCurrent([8,1,2,2,3]))