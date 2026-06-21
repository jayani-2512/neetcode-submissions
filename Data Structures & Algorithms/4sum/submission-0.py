class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=set()

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):
                        s=nums[i]+nums[j]+nums[k]+nums[l]
                        if s==target:
                            res.add((nums[i],nums[j],nums[k],nums[l]))
        return list(res)
