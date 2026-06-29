class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 1:
            return True

        cleaned = []

        for c in s:
            if c.isalnum():
                cleaned.append(c.lower())
        
        
        return cleaned == cleaned[::-1]