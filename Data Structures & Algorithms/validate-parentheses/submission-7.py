class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        opened = ["[", "{", "("]
        closed = ["]", "}", ")"]
        
        for i in range (len(s)):
            char = s[i]
            if char in opened:
                st.append(char)
            else:
                if (len(st) == 0):
                    return False
                if closed.index(char) == opened.index(st[-1]):
                    st.pop()
                else:
                    return False
        return len(st) == 0


                