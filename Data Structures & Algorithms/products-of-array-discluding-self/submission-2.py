class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0]*n
        suff = [0]*n
        res = [0]*n
        # nothing to the left of i = 0
        pref[0] = 1
        # nothing to the right of i = n - 1
        suff[n-1] = 1

        for i in range(1,n):
            pref[i] = nums[i-1]*pref[i-1]
        for i in range(n-2,-1, -1):
            suff[i] = nums[i + 1]*suff[i+1]
        for i in range(n):
            res[i] = pref[i]*suff[i]
        return res