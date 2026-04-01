class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxP

# only r keeps only going forward, not l
# l will only change when a value of r is found lesser than l and l = r 
# tc : O(n) and sc: O(n)