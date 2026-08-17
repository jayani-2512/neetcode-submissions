class Solution:
    def numSquares(self, n: int) -> int:
        dp=[n]*(n+1)
        dp[0]=0
        for k in range(1,n+1):
            for s in range(1,k+1):
                sq=s*s
                if k-sq<0:
                    break
                dp[k]=min(dp[k],1+dp[k-sq])
        return dp[n]