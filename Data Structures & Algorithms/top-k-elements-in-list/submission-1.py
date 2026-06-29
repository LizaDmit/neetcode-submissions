class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        if k==1:
            return [max(count, key=count.get)]
        for i in range(k):
            n = max(count, key=count.get)
            ans.append(n)
            count[n] = 0

        return ans
        

