class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        k = 0

        for i in range(len(temperatures)):
            while temperatures[i] >= temperatures[k+i]:
                k += 1
                if k + i == len(temperatures):
                    k = 0
                    break
            res.append(k)
            k = 0
        return res


