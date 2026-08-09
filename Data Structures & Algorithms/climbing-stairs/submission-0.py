class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*n
        def dfs(k):
            if k>=n:
                return k==n
            if dp[k]!=-1:
                return dp[k]
            dp[k]=dfs(k+1)+dfs(k+2)
            return dp[k]
        return dfs(0)