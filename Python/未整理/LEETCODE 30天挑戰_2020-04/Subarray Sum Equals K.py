from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        dic[0]=1
        sum1=0
        print(dic)
        count=0
        
        for i in range(len(nums)):
            sum1+=nums[i]
            if sum1-k in dic:
                count+=dic[sum1-k]
                print(count)
            if sum1 in dic:
                dic[sum1]+=1
                print(dic)
            else:
                dic[sum1]=1
                print(dic)
                
        return count


#print(Solution().subarraySum([1,1,1,1], 2))
#print(Solution().subarraySum([0,1,-1,1,1], 2))
#print(Solution().subarraySum([0,0,0,2,0], 2))
#print(Solution().subarraySum([1,5,1,-50], 2))
#print(Solution().subarraySum([-1,1,5,1,-50,1,3,1,1,-2], 2))
print(Solution().subarraySum([1,2,3,2,5,9,10,15,20,-50], 7))
##class Solution:
##    def subarraySum(self, nums: List[int], k: int) -> int:
##        ans = 0
##        for i in range(len(nums)):
##            Sum = 0
##            for j in range(i, len(nums)):
##                Sum += nums[j]
##                if Sum == k:
##                    ans += 1
##        return ans
