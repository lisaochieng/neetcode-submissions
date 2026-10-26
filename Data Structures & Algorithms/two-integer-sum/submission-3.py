class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store key: complement, and val: indx
        hmap = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in hmap:
                return [hmap[complement], i]
            hmap[num] = i

