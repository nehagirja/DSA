class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #makes the heap of size k 
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        #makes the heap of size k+1, then removes the smallest
        heapq.heappush(self.minHeap, val) #only the necessary swaps happen
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

#time complexity O(m * log n)



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)