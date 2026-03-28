class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() #O(n log n)
        res = []
        
        for i in range(len(nums)): #O(n)
            if i > 0 and nums[i-1] == nums[i]: #to avoid duplication at the first step. 
                continue

            l, r = i + 1, len(nums) - 1 
            while l < r: #O(n)
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1 
                    r -= 1 #if you don't have these two lines, it will cause an infinite loop
                    while l < r and nums[l] == nums[l-1]:
                        l += 1 #this is to prevent duplication in the next later (j,k)
        return res

        # TC : O(n2)
        # SC: O(1)

#IMP! if we have the j value, then we know we will be getting the same k value as well. that is why we only change the j value so that k value is changed by default because we will get a different sum and triplet for the next one. 
                
            