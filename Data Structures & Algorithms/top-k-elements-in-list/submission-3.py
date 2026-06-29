class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqTable = 2001*[0]

        for num in nums:
            freqTable[num + 1000] += 1

        ans = []
        for i in range (k):
            maxF = max(freqTable)
            maxE = freqTable.index(maxF)

            ans.append(maxE - 1000)
            freqTable[maxE] = 0

        return ans
        
