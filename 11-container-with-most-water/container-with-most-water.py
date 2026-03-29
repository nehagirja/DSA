class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height)-1
        while left < right:
            minValue =  min(height[left], height[right])
            area = (right - left) * minValue
            res = max(area, res)
            if minValue == height[left]:
                left += 1
            elif minValue == height[right]:
                right -= 1
        return res
            