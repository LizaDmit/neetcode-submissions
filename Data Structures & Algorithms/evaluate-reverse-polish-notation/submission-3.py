class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        i = 1
  

        while len(tokens) > 1:
          
            if tokens[i] != "+" and tokens[i] != "-" and tokens[i] != "*" and tokens[i] != "/":
                i += 1
                continue
            else:
                if tokens[i] == "+":
                    tokens[i-1] = int(tokens[i-2]) + int(tokens[i-1])
                elif tokens[i] == "-":
                    tokens[i-1] = int(tokens[i-2]) - int(tokens[i-1])
                elif tokens[i] == "*":
                    tokens[i-1] = int(tokens[i-2]) * int(tokens[i-1])
                elif tokens[i] == "/":
                    tokens[i-1] = int(tokens[i-2]) / int(tokens[i-1])
                
                tokens.pop(i-2)
                tokens.pop(i-1)

               
                i = 1

            
        return int(tokens[0])
            