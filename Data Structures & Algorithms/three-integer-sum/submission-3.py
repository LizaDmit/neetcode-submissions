class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        print(nums)

        for left in range(0, len(nums) - 2):
            mid, right = left + 1, len(nums) - 1

            while left < mid and mid < right:
                summ = nums[left] + nums[mid] + nums[right]
                if summ > 0:
                    right -= 1          
                elif summ < 0:
                    mid += 1
                else:
                    a = [nums[left], nums[mid], nums[right]]
                    if a not in ans:
                        ans.append(a)
                    right -= 1
                    
                    
        return ans