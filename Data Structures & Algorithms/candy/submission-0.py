class Solution:
    def candy(self, ratings: List[int]) -> int:
        count=len(ratings)
        i=1
        while i<len(ratings):
            if ratings[i]==ratings[i-1]:
                i+=1
                continue
            inc=0
            while i<len(ratings) and ratings[i]>ratings[i-1]:
                inc+=1
                count+=inc
                i+=1
            dec=0
            while i<len(ratings) and ratings[i]<ratings[i-1]:
                dec+=1
                count+=dec
                i+=1
            count-=min(inc,dec)
        return count
        