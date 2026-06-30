class Solution:
    def isPalindrome(self, s: str) -> bool:
        plr = 0
        prl = len(s) - 1

        while plr <= prl:
            while plr < len(s) and not s[plr].isalnum():
                plr += 1
            while prl > -1 and not s[prl].isalnum():
                prl -= 1

            if plr >= prl:
                return True

            if s[plr].lower() != s[prl].lower():
                return False
                
            plr += 1
            prl -= 1
        
        return True