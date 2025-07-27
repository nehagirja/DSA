class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans

    #    n = len(nums)
    #    ans = [0] * 2 * n 
    #    for i in range(len(nums)):
    #         ans[i+n] = ans[i] = nums[i]
    #    return ans

    # for when, asked to iterate x times 