class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        nums.sort()


        for left in range(0, len(nums) - 2):
            mid, right = left + 1, len(nums) - 1
            if nums[left] > 0:
                break
            if left != 0 and nums[left] == nums[left - 1]:
                continue

            while mid < right:
                summ = nums[left] + nums[mid] + nums[right]
                if summ > 0:
                    right -= 1          
                elif summ < 0:
                    mid += 1
                else:
                    a = [nums[left], nums[mid], nums[right]]

                    ans.append(a)
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    mid += 1
                    right -= 1
                    
                    
        return ans




        