class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for item in s:
            if item == "(" or item == "[" or item == "{":
                stack.append(item)
            elif (item == ")" or item == "]" or item == "}") and len(stack) == 0:
                return False
            elif item == ")":
                if "(" not in stack:
                    return False
                elif stack[-1] == "(":
                    stack.pop()
            elif item == "]":
                if "[" not in stack:
                    return False
                elif stack[-1] == "[":
                    stack.pop()
            elif item == "}":
                if "{" not in stack:
                    return False
                elif stack[-1] == "{":
                    stack.pop()

        return len(stack) == 0
        