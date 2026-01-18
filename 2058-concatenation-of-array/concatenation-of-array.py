class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums[:len(nums)] 
        for n in nums:
            ans.append(n)
        return ans