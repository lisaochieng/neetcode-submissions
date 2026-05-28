class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            counts = Counter(word)
            hashkeys = tuple(sorted(counts.items()))

            groups[hashkeys].append(word)

        results = list(groups.values())

        return results
