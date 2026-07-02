# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r=1,n
        while True:
            mid1=l+(r-l)//3
            mid2=r-(r-l)//3
            if guess(mid1)==0:
                return mid1
            elif guess(mid2)==0:
                return mid2
            elif guess(mid1)+guess(mid2)==0:
                l=mid1+1
                r=mid2-1
            elif guess(mid1)==-1:
                r=mid1-1
            else:
                l=mid2+1
            