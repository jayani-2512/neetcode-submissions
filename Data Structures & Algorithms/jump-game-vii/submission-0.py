class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n=len(s)
        can=[False]*n
        can[0]=True
        j=0
        for i in range(n):
            if can[i]==False:
                continue
            j=max(j,i+minJump)
            while j<min(i+maxJump+1,n):
                if s[j]=='0':
                    can[j]=True
                j+=1
        return can[n-1]