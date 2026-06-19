class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        n=len(word1)
        m=len(word2)
        res=""
        while(i<n and j<m):
            res+=word1[i]+word2[j]
            i+=1
            j+=1
        if(len(word1)>len(word2)):
            for i in range(m,n):
                res+=word1[i]
        if(len(word2)>len(word1)):
            for i in range(n,m):
                res+=word2[i]
        return res
