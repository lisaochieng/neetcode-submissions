class Solution:
    import heapq
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []
        maxheap =  [(count, item) for item, count in counts.items()]
        heapq.heapify_max(maxheap)
        for i in range(k):
            count, item = heapq.heappop_max(maxheap)
            res.append(item)

        return res

        
        