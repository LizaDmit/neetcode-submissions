class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l
        left = [1] * l
        right = [1] * l
        

        for i in range(1,l):
            left[i] = nums[i-1] * left[i-1]
            right[-1-i] = nums[-i] * right[-i] 
        for i in range(l):
            res[i] = left[i]*right[i]

         

        return res




            
        