class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[l - 1]:
                nums[l] = nums[r]
                l += 1
        return l


# l is the placeholder - first replace, then increment 
# r compares only 
# TC O(n)