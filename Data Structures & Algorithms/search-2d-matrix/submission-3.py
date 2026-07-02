class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,0
        while l<len(matrix) and r<len(matrix[0]):
            if matrix[l][r]==target:
                return True
            r+=1
            if r==len(matrix[0]):
                l+=1
                r=0
        return False
