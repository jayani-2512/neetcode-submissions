class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(len(prices)):
            b=prices[i]
            for j in range(i+1,len(prices)):
                s=prices[j]
                profit=max(profit,s-b)
        return profit
