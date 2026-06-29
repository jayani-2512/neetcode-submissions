class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for n in tokens:
            if n not in "+*-/":
                stack.append(int(n))
            elif n == "+":
                stack.append(stack.pop()+stack.pop())
            elif n == "-":
                r=stack.pop()
                l=stack.pop()
                s=l-r
                stack.append(s)
            elif n == "*":
                stack.append(stack.pop()*stack.pop())
            elif n == "/":
                r=stack.pop()
                l=stack.pop()
                stack.append(int(float(l)/r))
        return stack[-1]
            