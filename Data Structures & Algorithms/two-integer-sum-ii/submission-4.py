class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap=defaultdict(int)
        for i in range(len(numbers)):
            diff = target-numbers[i]
            if hashmap[diff]:
                return [hashmap[diff],i+1]
            hashmap[numbers[i]]=i+1
        return []