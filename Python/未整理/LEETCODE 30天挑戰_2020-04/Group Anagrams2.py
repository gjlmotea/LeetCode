from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            if tuple(sorted(string)) not in groups:
                groups[tuple(sorted(string))] = list()
            groups[tuple(sorted(string))].append(string)
            
        return groups.values()

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

##from typing import List
##from collections import defaultdict
##class Solution:
##    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
##        groups = defaultdict(list)
##        for string in strs:
##            groups[tuple(sorted(string))].append(string)
##            
##        return groups.values()
