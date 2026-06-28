class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        for n in operations:
            if n not in ["+","C","D"]:
                record.append(int(n))
            elif n == "+":
                s= record[-1]+record[-2]
                record.append(s)
            elif n =="D":
                s1= 2*record[-1]
                record.append(s1)
            elif n =="C":
                record.pop()
        return sum(record)
        