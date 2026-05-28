class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = set(nums)
        if len(l)< len(nums):
            return True
        else:
            return False
         