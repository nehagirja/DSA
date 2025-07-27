class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
       n = len(nums)
       ans = [0] * 2 * n 
       for i in range(len(nums)):
            ans[i+n] = ans[i] = nums[i]
       return ans

# assign the length to the ans array 