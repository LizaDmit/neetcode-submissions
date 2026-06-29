class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        k = 0
        longest = 0

        for item in nums:

            if (item - 1) not in nums:
                k = 1
                while (item + k) in nums:
                    k += 1
            longest = max(k,longest)
                
        return longest