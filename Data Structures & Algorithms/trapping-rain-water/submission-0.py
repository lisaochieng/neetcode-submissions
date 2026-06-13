class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        maxleft = [0]*n
        maxright = [0]*n

        maxleft[0] = height[0]

        for i in range(1, n):
            maxleft[i] = max(height[i], maxleft[i-1])
        
        maxright[n-1] = height[n-1]
        for i in range(n-2,-1, -1):
            maxright[i] = max(height[i], maxright[i+1])

        res = 0
        for i in range(n):
            cap = min(maxleft[i], maxright[i]) - height[i]
            if cap < 0:
                cap == 0
            res += cap

        return res



        