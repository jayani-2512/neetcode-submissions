class Solution:
    def checkValidString(self, s: str) -> bool:
        minleft=0
        maxleft=0
        for c in s:
            if c=="(":
                minleft+=1
                maxleft+=1
            elif c==")":
                minleft-=1
                maxleft-=1
            else:
                minleft-=1
                maxleft+=1
            if minleft<0:
                minleft=0
            if maxleft<0:
                return False
        return minleft==0