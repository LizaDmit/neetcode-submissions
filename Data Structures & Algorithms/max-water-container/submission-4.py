class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxV = 0

        while left < right:
            curV = min(heights[left], heights[right])*(right - left)
            maxV = max(maxV, curV)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxV
