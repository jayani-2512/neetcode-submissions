class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[-1]*len(cost)
        def dfs(k):
            if k>=len(cost):
                return 0
            if dp[k]!=-1:
                return dp[k]
            dp[k]=cost[k]+min(dfs(k+1),dfs(k+2))
            return dp[k]
        return min(dfs(0),dfs(1))