class Solution:
    def numDecodings(self, s: str) -> int:
        dp={len(s):1}
        def dfs(k):
            if k in dp:
                return dp[k]
            if s[k]=='0':
                return 0
            res=dfs(k+1)
            if k+1<len(s) and (s[k]=='1'or s[k]=='2' and s[k+1] in          '0123456'):
                res+=dfs(k+2)
            dp[k]=res
            return res
        return dfs(0)