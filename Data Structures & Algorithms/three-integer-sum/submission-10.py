class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        

        for start in range (0, len(nums) - 2):
            if start != 0 and nums[start - 1] == nums[start]: 
                continue
            left = start + 1
            right = len(nums) - 1

            while left < right:
                curSum = nums[start] + nums[left] + nums[right]

                if curSum == 0:
                    ans.append([nums[start], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif curSum < 0:
                    left += 1
                else:
                    right -= 1


            
        return ans
                
