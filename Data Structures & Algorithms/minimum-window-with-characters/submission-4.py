class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mpt = {}
        for i in range (len(t)):
            if t[i] not in mpt:
                mpt[t[i]] = 0
            mpt[t[i]] += 1
        mp = {}
        for i in range (len(t)):
            mp[t[i]] = 0

        minL = 1001
        minS = 0
        minE = 0
        start = 0

        for end in range (len(s)):
            while (start < len(s) and s[start] not in mp):
                start += 1
            if s[end] not in mp:
                continue

            mp[s[end]] += 1
     
            while all(mp[c] >= mpt[c] for c in mpt):
                if (minL > end - start + 1):
                    minS = start
                    minE = end
                minL = min(minL, end - start + 1)
                if (s[start] in mp):
                    mp[s[start]] -= 1
                start += 1

        if minL == 1001: 
            return ""
        return s[minS : minE + 1]