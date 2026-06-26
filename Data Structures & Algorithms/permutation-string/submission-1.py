class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1={}
        for i in range(len(s1)):
            count1[s1[i]]=1+count1.get(s1[i],0)
        len1=len(count1)

        for i in range(len(s2)):
            count2, len2={},0
            for j in range(i,len(s2)):
                count2[s2[j]]=1+count2.get(s2[j],0)
                if count1.get(s2[j],0)<count2.get(s2[j],0):
                    break
                if count1.get(s2[j],0)==count2.get(s2[j],0):
                    len2+=1
                if len1==len2:
                    return True
        return False