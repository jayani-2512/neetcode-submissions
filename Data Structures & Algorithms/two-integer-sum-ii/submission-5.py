class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        n=len(numbers)
        while l<r:
            tmp=numbers[l]+numbers[r]
            if tmp==target:
                return [l+1,r+1]
            elif tmp<target:
                l+=1
            else:
                r-=1
        return []
