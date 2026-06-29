class Solution:

    def __init__(self):
        self.count = []

    def encode(self, strs: List[str]) -> str:

        for i in range(len(strs)):
            self.count.append(len(strs[i]))

        return "".join(strs)

    def decode(self, s: str) -> List[str]:

        res = []
        k = 0
        for i in range(len(self.count)):
            res.append(s[k:k+self.count[i]])
            k += self.count[i]

        return res
