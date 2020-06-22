from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        ans = []
        for string in strs:
            str_in_groups = False
            for g_index in groups:
                #print(group[g_index])
                if set(string) == groups[g_index]:
                    str_in_groups = True
                    ans[g_index].append(string)
                    break
            if str_in_groups:
                pass
            else:
                groups[len(groups)] = set(string)
                ans.append(list())
                ans[len(groups)-1].append(string)
        return ans
        

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

'''
"boo"與"bob"居然是在不同類別
'''
