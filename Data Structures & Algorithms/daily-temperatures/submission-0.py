class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res=[]
        for i in range(n):
            c=1
            j=i+1
            while j<n:
                if temperatures[j]>temperatures[i]:
                    break
                j+=1
                c+=1
            c=0 if j==n else c
            res.append(c)
        return res