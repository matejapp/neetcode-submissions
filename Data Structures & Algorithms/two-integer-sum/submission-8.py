class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Initalize empty hashMap
        mySet = {}

        #Loop thru the numbers and indexes of the array
        for i, n in enumerate(nums):
            #Define the needed value
            needed = target - n

            #Check if that value is in map
            if needed in mySet:
                return [mySet[needed], i]
            
            mySet[n] = i
            

        return []