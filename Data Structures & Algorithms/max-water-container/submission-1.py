class Solution(object):
    def maxArea(self, height):
        
        left, right = 0, len(height) - 1
        vol_max = min(height[left],height[right])*(right - left)

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
            vol = min(height[left],height[right])*(right - left)
            if vol > vol_max:
                vol_max = vol
            
        return vol_max
        