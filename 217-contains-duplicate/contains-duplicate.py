class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set(nums)

        if len(hashSet) == len(nums):
            return False
        return True