class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        oper = ["+", "-", "*", "/"]

        for item in tokens:
            if item not in oper:
                stack.append(int(item))
            else:
                m = stack.pop()
                n = stack.pop()
                if item == "+":
                    stack.append(n+m)
                elif item == "-":
                    stack.append(n-m)
                elif item == "*":
                    stack.append(n*m)
                else:
                    stack.append(int(n/m))
      



            
        return stack[0]
            
            