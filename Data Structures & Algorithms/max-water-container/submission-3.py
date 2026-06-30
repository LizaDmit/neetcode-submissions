class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        curV = min(heights[left], heights[right])*(right - left)
        maxV = curV

        while left < right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            curV = min(heights[left], heights[right])*(right - left)
            maxV = max(maxV, curV)

        return maxV
