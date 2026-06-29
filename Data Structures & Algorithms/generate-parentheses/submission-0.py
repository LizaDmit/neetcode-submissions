class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generate(str, opn, cls, res):

        
            if len(str) == 2*n:
                res.append(str)
                return
            else:
                if opn < n:
                    generate(str + "(", opn + 1, cls, res)
                if cls < opn:
                    generate(str + ")", opn, cls + 1, res)
        ans = []
        generate("", 0, 0,ans)
        return ans



            
            




            
        

