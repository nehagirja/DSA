class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set(nums)
        if len(nums) == len(seen):
            return False
        return True