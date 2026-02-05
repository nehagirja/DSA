class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else: 
                return mid 
        return -1 
# Notes: If l or r is only mid and not mid + 1 or mid - 1 respectively then it goes into an infinite loop in cases where l and r are close ex: 3,4 mid = 3, never ending loop pecause l never becomes l > = r 