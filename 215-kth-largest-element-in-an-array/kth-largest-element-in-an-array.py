class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # minHeap = []

        # for n in nums:
        #     heapq.heappush(minHeap, n)
        #     if len(minHeap) > k:
        #         heapq.heappop(minHeap)
            
        # return minHeap[0]

        # Internally using a library solution:

        return heapq.nlargest(k, nums) [-1]
        
        # time complexity = O(n logk )

