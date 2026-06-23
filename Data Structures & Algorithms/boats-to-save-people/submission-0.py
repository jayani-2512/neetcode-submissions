class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count=0
        people.sort()
        l,r=0,len(people)-1
        while l<=r:
            rest=limit-people[r]
            r-=1
            count+=1
            if l<=r and rest>=people[l]:
                l+=1

        return count