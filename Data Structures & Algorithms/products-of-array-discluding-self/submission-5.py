class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_right = []
        plr = 1
        right_left = []
        prl = 1

        for i in range (len(nums)):
            plr *= nums[i]
            left_right.append(plr)

        for i in range (len(nums)):
            prl *= nums[len(nums) - i - 1]
            right_left.insert(0, prl)

        ans = []
        ans.append(right_left[1])
        for i in range (1, len(nums) - 1):
            ans.append(left_right[i - 1]*right_left[i + 1])
        ans.append(left_right[-2])

        return ans

