class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsOrig = set()
        for i in range (len(nums)):
            if nums[i] in numsOrig:
                return True
            numsOrig.add(nums[i])
        return False