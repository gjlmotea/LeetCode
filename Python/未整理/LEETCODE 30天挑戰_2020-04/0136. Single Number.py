from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = set()
        for integer in nums:
            if integer in single_num:
                single_num.remove(integer)
            else:
                single_num.add(integer)
        return list(single_num)

print(Solution.singleNumber(object(), [2,2,1]))
