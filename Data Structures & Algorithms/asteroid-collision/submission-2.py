class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for n in asteroids:
            while stack and stack[-1]>0 and n<0:
                d=n+stack[-1]
                if d<0:
                    stack.pop()
                elif d>0:
                    n=0
                else:
                    n=0
                    stack.pop()
            if n:
                stack.append(n)
        return stack
