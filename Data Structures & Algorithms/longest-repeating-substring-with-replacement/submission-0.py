class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen=0
        for i in range(len(s)):
            count={}
            freq=0
            for j in range(i,len(s)):
                count[s[j]]=1+count.get(s[j],0)
                freq=max(freq,count[s[j]])
                ch = (j-i+1)- freq
                if ch<=k:
                    maxlen=max(maxlen,j-i+1)
                else:
                    break
        return maxlen

