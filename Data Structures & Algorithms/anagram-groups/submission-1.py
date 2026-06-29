class Solution:

    def AnagramLetters(self, s):

        l = len(s)
        alphabet = [0]*26

        for i in range (l):
            alphabet[ord(s[i]) - ord('a')] += 1

        return tuple(alphabet)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for s in strs:
            key = self.AnagramLetters(s)
            if key not in ans:
                ans[key] = []
            ans[key].append(s)

        return list(ans.values())
            



