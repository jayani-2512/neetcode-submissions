class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[1]=1
        for k in range(1,n+1):
            dp[k]=0 if k==n else k
            for i in range(1,k+1):
                dp[k]=max(dp[k],dp[i]*dp[k-i])
        return dp[n]