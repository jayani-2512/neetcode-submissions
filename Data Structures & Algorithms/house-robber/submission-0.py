class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n)
        
        def dfs(k):
            if k>=n:
                return 0
            if dp[k]!=-1:
                return dp[k]
            dp[k]=max(dfs(k+1),nums[k]+dfs(k+2))
            return dp[k]
        return dfs(0)
