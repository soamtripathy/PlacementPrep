def search(nums, target):
    n = len(nums)
    l = 0
    h = n-1
    while l <= h:
        m = l + (h-l)//2
        if nums[m] == target:
            return m
        if target >= nums[0] and nums[m] < nums[0]:
            h = m-1
        elif target < nums[0] and nums[m] >= nums[0]:
            l = m+1
        else:
            if nums[m] < target:
                l = m+1
            else:
                h = m-1
    return -1
print(search([4,5,6,7,0,1,2], 0))
