class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        left = 0
        right = 1

        while right < len(prices):
            if (prices[right] > prices[left]):
                p = prices[right] - prices[left]
                maxP = max(maxP, p)
            else:
                left = right
            right += 1

        return maxP

