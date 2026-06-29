class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        for i,n in enumerate(nums):
            del nums[i]
            prod = 1
            for num in nums:
                prod *= num

            output.append(prod)
            nums.insert(i,n)
        
        return output