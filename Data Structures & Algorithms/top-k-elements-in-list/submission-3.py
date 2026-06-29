
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Base case
        if(len(nums) == 0):
            return []
        if(len(nums) == 1):
            return nums

        isSeen = {}

        for n in nums:

            if n not in isSeen:
                isSeen[n] = 0

            isSeen[n] += 1

        res = sorted(isSeen, key = isSeen.get, reverse = True)[:k]
        return res
        