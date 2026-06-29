class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums.sort()
        print(nums)
        options = []
        k = 1
        i = 1


        while i < len(nums):
            if nums[i] == nums[i-1]:
                if i == len(nums) - 1:
                    options.append(k)
                else:
                    pass
            elif nums[i] - nums[i-1] == 1:
                k += 1

                if i == len(nums) - 1:
                    options.append(k)

            else:
                options.append(k)
                k = 1
            i += 1

        if options == []:
            return k
        return max(options)

        