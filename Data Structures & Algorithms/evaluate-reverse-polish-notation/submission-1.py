class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for n in tokens:
            if n not in "+*-/":
                stack.append(int(n))
            elif n == "+":
                r=stack.pop()
                l=stack.pop()
                s=l+r
                stack.append(s)
            elif n == "-":
                r=stack.pop()
                l=stack.pop()
                s=l-r
                stack.append(s)
            elif n == "*":
                r=stack.pop()
                l=stack.pop()
                s=l*r
                stack.append(s)
            elif n == "/":
                r=stack.pop()
                l=stack.pop()
                s=l/r
                stack.append(int(s))
        return stack[-1]
            