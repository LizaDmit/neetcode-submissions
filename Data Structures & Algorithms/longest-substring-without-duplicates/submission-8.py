class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (s == ""):
            return 0
        mp = {}
        start = 0
        maxl = 1

        for i in range (len(s)):
            k = ord(s[i]) - ord('a')
            if k in mp:
                start = max(start, mp[k] + 1)
            mp[k] = i
            maxl = max(maxl,i - start + 1)

        return maxl


