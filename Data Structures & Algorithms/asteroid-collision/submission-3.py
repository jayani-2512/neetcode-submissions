class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n=len(asteroids)
        j=-1
        for n in asteroids:
            while j>=0 and asteroids[j]>0 and n<0:
                if asteroids[j]>abs(n):
                    n=0
                    break
                elif asteroids[j]==abs(n):
                    j-=1
                    n=0
                    break
                else:
                    j-=1
            if n:
                j+=1
                asteroids[j]=n
        return asteroids[:j+1]