class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join([char for char in s if char.isalnum()]).lower()
        revcleaned = cleaned[::-1]
        if revcleaned == cleaned:
            return True
        return False