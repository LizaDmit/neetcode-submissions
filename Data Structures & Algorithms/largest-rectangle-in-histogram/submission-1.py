class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        vals = set()
        maxx = 0


        for i in range(len(heights)):
            curr_height = heights[i]

            if curr_height  not in vals:
                vals.add(curr_height)

                count = 0
                for j in range(len(heights)):
                    if heights[j] < curr_height:
                        count = 0
                    else:
                        count += 1
                    if curr_height * count > maxx:
                        maxx = heights[i] * count
        return maxx