class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        counts = {}
        res = []
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        for i in range(len(nums)):
            counts[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                counts[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                third = -(nums[i] + nums[j])
                if counts.get(third, 0) > 0:
                    res.append([nums[i], nums[j], third])
            
            for j in range(i+1, len(nums)):
                counts[nums[j]] += 1
        return res
            