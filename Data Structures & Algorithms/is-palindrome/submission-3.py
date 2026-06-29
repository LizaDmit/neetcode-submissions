class Solution:
    def isPalindrome(self, s: str) -> bool:

        n = len(s)

        left = 0
        right = n - 1
        symbols = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [str(i) for i in range(10)]

        while left <= right:

            while s[left].lower() not in symbols and left < right:
                left += 1
            while s[right].lower() not in symbols and right > left:
                right -= 1
            if s[left].lower() != s[right].lower():
                 return False
            left += 1
            right -= 1
        return True
        


        
        


        