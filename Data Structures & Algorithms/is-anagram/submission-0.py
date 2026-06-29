class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       t = list(t)
       t.sort()
       s = list(s)
       s.sort()
       return s == t
