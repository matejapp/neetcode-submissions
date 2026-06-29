class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #Base case
        if(len(strs) == 1):
            return [strs]
        if(len(strs) == 0):
            return [[]]
        
        groups = {}

        #Sort individual strings
        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] =[]

            groups[key].append(word)

    
        return list(groups.values())





