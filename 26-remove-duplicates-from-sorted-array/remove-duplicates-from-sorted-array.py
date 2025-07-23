class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)

# Set insertion takes O(1) time complexity
# Sorted - O(nlogn)
# Slicing - O(n)
# Sorting dominated - Hence, O( nlogn)