class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = defaultdict(int)
        for char in s:
            smap[char] += 1
        tmap = defaultdict(int)
        for char in t:
            tmap[char] += 1
            
        if smap == tmap:
            return True
        return False