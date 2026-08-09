class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[-1]*(n+1)
        def dfs(k):
            if k<=2:
                return 1 if k!=0 else 0 
            if dp[k]!=-1:
                return dp[k]
            dp[k]=dfs(k-1)+dfs(k-2)+dfs(k-3)
            return dp[k]
        return dfs(n)