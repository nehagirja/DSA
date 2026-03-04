class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap) #O(n)
        
        val = 0
        while k > 0:
            val = heapq.heappop(maxHeap)
            k -= 1

        return val * -1
            


