class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area=0
        stack=[]

        for i,h in enumerate(heights):
            s=i
            while stack and stack[-1][1]>h:
                n,l=stack.pop()
                area=max(area,l*(i-n))
                s=n
            stack.append((s,h))
        
        for n,l in stack:
            area=max(area,l*(len(heights)-n))
        return area