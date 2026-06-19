class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=list(s)
        l,r=0,len(s1)-1
        while(l<r):
            if not s1[l].isalnum():
                l+=1
                continue
            if not s1[r].isalnum():
                r-=1
                continue
            if(s1[l].lower()!=s1[r].lower()):
                return False
            l+=1
            r-=1
        return True
