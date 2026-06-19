class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        m=len(s)//2
        for i in range(m):
            temp=s[i]
            s[i]=s[n-i-1]
            s[n-i-1]=temp
            