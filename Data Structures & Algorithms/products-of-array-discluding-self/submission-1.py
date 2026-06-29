class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) == len(nums):
            return [0] * len(nums)
        product = 1
        res = [] 
        zeroes = nums.count(0)
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]

        for i in range(len(nums)):
            if (zeroes > 0 and nums[i] != 0) or zeroes > 1:
                res.append(0)
            elif nums[i] == 0 and zeroes == 1 :
                res.append(product)
            else:
                res.append(int(product/nums[i]))

        return res




            
        




            
        


        