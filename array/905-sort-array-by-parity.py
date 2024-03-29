class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # a=[]
        # for i in nums:
        #     if i%2==0:
        #         a.insert(0,i)
        #     else:
        #         a.append(i)
        # return a
        odd   = len(nums) - 1        
        index = 0
        
        while odd > index:
            
            num = nums[index]
            
			#if even we move the left pointer
            if num % 2 == 0:
                index += 1
                continue
            #otherwise if odd we swap and move odd to left and in next iteration check 
			#the new value which is now placed in current index
            nums[odd], nums[index] = nums[index],nums[odd]
            odd -= 1
        
        return nums