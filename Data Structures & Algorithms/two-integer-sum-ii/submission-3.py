class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            comp = target - numbers[i]

            lo = 0
            hi = len(numbers) - 1
            
            while lo <= hi:
                mid = lo + (hi - lo)//2
                if numbers[mid] == comp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < comp:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return []