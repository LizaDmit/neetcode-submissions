class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        for item in strs:
            sorted_item = "".join(sorted(item))
            if sorted_item not in groups:
                groups[sorted_item] = [item]
            else:
                groups[sorted_item].append(item)
        return list(groups.values())


        