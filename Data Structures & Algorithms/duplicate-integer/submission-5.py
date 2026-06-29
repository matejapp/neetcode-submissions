class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = {n for n in nums}
        return len(res) != len(nums)
        