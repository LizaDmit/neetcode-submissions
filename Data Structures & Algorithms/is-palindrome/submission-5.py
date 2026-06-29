class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = ""

        for item in s:
            if item.isalnum():
                new_s += item.lower()
        return new_s == new_s[::-1]
