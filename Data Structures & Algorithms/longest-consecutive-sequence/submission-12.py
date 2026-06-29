class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sorted_nums = sorted(nums)

        k = 1
        max_streak = 1

        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i + 1] == sorted_nums[i]:
                continue

            elif sorted_nums[i + 1] - sorted_nums[i] == 1:
                k += 1

            else:
                k = 1

            if k > max_streak:
                max_streak = k

        return max_streak