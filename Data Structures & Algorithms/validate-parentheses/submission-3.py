class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for n in s:
            if n in "({[":
                stack.append(n)
            elif stack and stack[-1]=="(" and n ==")":
                stack.pop()
            elif stack and stack[-1]=="{" and n =="}":
                stack.pop()
            elif stack and stack[-1]=="[" and n =="]":
                stack.pop()
            else:
                return False
        return len(stack)==0