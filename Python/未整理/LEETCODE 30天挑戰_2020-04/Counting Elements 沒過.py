from typing import List
class Solution:
    def countElements(self, arr: List[int]) -> int:
        int_set = set()
        ans = 0
        for integer in arr:
            int_set.add(integer)
            if integer+1 in int_set:
               ans += 1
               int_set.remove(integer+1)
               print("========: ", integer+1)
            if integer-1 in int_set:
               ans += 1
               int_set.remove(integer-1)
               print("========: ", integer-1)
        return ans


print(Solution().countElements([1,1,2,2]))
print(tuple([1,1,2,3,2,5]))
