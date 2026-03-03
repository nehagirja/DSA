class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones] # there is no maxHeap in python hence take -ve of all vals
        heapq.heapify(stones)

        while len(stones) > 1:
            #pop values in any case 
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second) #adding a new value that is the difference of the first 2 
            
        stones.append(0) #adding 0 if eventually no values are left, aka 0 values in list 
        return abs(stones[0]) #absolute value conversion 




            

