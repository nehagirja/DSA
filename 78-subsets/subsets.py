class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy()) #creates a new list with the same elements/snapshot. 
                return
            
            subset.append(nums[i])  
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res 