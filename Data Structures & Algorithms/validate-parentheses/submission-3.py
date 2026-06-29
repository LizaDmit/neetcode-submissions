class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for item in s:
            if item in closeToOpen:
                if len(stack) != 0 and stack[-1] == closeToOpen[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        
        return True if not stack else False
        