def binarySearch(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = left + (right-left//2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < mid:
            mid = left+1
        else:
            mid = right-1
    return -1
print(binarySearch([-1,0,3,5,9,12], 0))
