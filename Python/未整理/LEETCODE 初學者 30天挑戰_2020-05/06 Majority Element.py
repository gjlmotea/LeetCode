from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numDict = {}
        for num in nums:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
        for n in numDict:
            if numDict[n] >= len(nums)//2 + 1:
                return n

print(Solution().majorityElement([3,2,3]))
print(Solution().majorityElement([2,2,1,1,1,2,2]))


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        print(counts)
        for item in counts.items():
            print(item)
            if item[1] > len(nums) // 2:
                return item[0]



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # majority element is the element that appears more
        #than n/2 times
        nums.sort() 
        majority = nums[int(len(nums)/2)]
        return majority
