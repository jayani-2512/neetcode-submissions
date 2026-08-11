class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        resi=0
        resl=0
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and ((j-i+1)<=2 or dp[i+1][j-1]==True):
                    dp[i][j]=True
                    if (j-i+1)>resl:
                        resl=j-i+1
                        resi=i
        return s[resi:resi+resl]