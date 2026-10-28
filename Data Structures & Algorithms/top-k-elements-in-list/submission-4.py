class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        res = []
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        sorted_dict = dict(sorted(counts.items(), key = lambda item: item[1], reverse = True))
        for i,key in enumerate(sorted_dict.keys()):
            if i < k:
                res.append(key)
        return res