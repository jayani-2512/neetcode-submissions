class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*n for _ in range(m)]
    
        def dfs(i,j):
            
            if i>=m or j>=n:
                return float("inf")
            if dp[i][j]!=-1:
                return dp[i][j]
            if i==m-1 and j==n-1:
                return grid[i][j]
            dp[i][j]=grid[i][j]+min(dfs(i+1,j),dfs(i,j+1))
            
            return dp[i][j]
        return dfs(0,0)