class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # sorted() returns a new sorted list of characters
        for c1, c2 in zip(sorted(s), sorted(t)):
            if c1 != c2:
                return False
                
        return True
