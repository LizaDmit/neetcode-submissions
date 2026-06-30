class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (s == ""):
            return 0
        mp = {}
        start = 0
        maxl = 1

        for i in range (len(s)):
            if s[i] in mp:
                start = max(start, mp[s[i]] + 1)
            mp[s[i]] = i
            maxl = max(maxl,i - start + 1)

        return maxl


