class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [1] * l

        plr = 1
        for i in range (l):
            ans[i] = plr
            plr *= nums[i]

        prl = 1
        for i in range (l - 1, - 1, -1):
            ans[i] *= prl
            prl *= nums[i]

        return ans