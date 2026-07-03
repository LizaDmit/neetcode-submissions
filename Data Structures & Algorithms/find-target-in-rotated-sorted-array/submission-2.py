class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right)//2

            if nums[mid] > nums[right]: # smallest in the rght half
                left = mid + 1  
            else: # smallest in the left half
                right = mid

        pivot = left

        if pivot == 0:
            left = 0
            right = len(nums) - 1
        elif nums[0] <= target:
            right = pivot - 1
            left = 0
        else:
            right = len(nums) - 1
            left = pivot
            
        while left < right:
            mid = (left + right)//2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] != target:
            return -1
            
        return left


