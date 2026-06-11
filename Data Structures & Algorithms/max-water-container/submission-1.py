class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        maxArea = 0
        while l < r:
            h = min(heights[l], heights[r])
            area = h * (r-l)
            maxArea = max(area, maxArea)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxArea


        