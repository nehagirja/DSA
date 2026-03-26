class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = 1
        res = [1] * len(nums)
    
        # prefix loop
        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1]
        # suffix loop 
        for i in range(len(nums)-2, -1, -1):
            suffix = suffix * nums[i+1]
            res[i] = suffix * res[i]
        return res 
            
        
                

# time complexity is O(n) and SC: O(n)








            
        
            
            