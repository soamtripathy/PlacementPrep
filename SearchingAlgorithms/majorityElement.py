'''boyer moore algorithm'''
# import collections


def majorityElement(nums):
    # d = dict(collections.Counter(nums))
    # n = len(nums)
    # for key, values in d.items():
    #     if d[key] > n/2:
    #         return key
    """
            Since the count of majority element will be atleast n//2 + 1 therefore,
            if we make a number as majorityElement and keep on incrementing the count if we encounter that element again and decrement the count if any other element is encountered then the majority element will have atleast 1 in count. Whenever the count becomes 0, reinitialise the majority element with current number.
            For example, nums = [2,2,1,1,1,2,2]
            Let's say majorityElement is 2 therefore count will be 1.
            Nove move ahead and again 2 is encountered so count will be incremented and become 2.
            Now 1 is encountered so count will be decremented and become 1
            Now again 1 is encountered so count will be decremented and become 0
            Now 1 is encountered but count is 0 so initialize 1 as majority element and count to 1 again.
            Now 2 is encountered so count will be decremented and become 0
            Now again 2 is encountered but count is 0 so initialize 2 as majority element and count to 1 again.
            Now no more elements are left so just return the majprity element.
        """
    count = 0
    majorElement = None
    for num in nums:
        if count == 0:
            majorElement = num
        count += 1 if majorElement == num else -1
    return majorElement


print(majorityElement([6, 5, 5]))
