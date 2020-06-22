from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        products = []
        for num in nums:
            total *=  num
        for n, num in enumerate(nums):
            if num != 0:
                result = total // num
            else:
                result = 1
                for i in range(len(nums)):
                    if i != n:
                        result *= nums[i]   
            products.append(result)
        return products


        
    

print(Solution().productExceptSelf([1,2,3,4]))
print(Solution().productExceptSelf([0,0]))
print(Solution().productExceptSelf([1,0]))

##
##class Solution:
##    def productExceptSelf(self, nums: List[int]) -> List[int]:
##        result = [1] * len(nums)
##        total = 1
##        for i in range(1, len(nums)):  # result[i] = nums[0] ... nums[i-1]
##            total *= nums[i-1]
##            result[i] = total
##        total = 1
##        for i in range(len(nums) - 2, -1, -1): # result[i] *= nums[-1] ... nums[i+1]
##            total *= nums[i+1]
##            result[i] *= total
##        
##        return result


##
##class Solution:
##    def productExceptSelf(self, nums: List[int]) -> List[int]:
##        result = [1] * len(nums)
##        total = 1
##        for i in range(1, len(nums)):  # result[i] = nums[0] ... nums[i-1]
##            total *= nums[i-1]
##            result[i] = total
##        total = 1
##        for i in range(len(nums) - 2, -1, -1):
##            total *= nums[i+1]
##            result[i] *= total
##        
##        return result
##            

##
##class Solution:
##    def productExceptSelf(self, nums: List[int]) -> List[int]:
##        output = [1] * len(nums)
##        
##        for i in range(1, len(nums)):
##            output[i] = output[i - 1] * nums[i - 1]
##            
##        R = 1
##        for i in reversed(range(0, len(nums))):
##            output[i] = output[i] * R
##            R = R * nums[i]
##
##        return output



##class Solution:
##    def productExceptSelf(self, nums: List[int]) -> List[int]:
##        
##        # The length of the input array 
##        length = len(nums)
##        
##        # The answer array to be returned
##        answer = [0]*length
##        
##        # answer[i] contains the product of all the elements to the left
##        # Note: for the element at index '0', there are no elements to the left,
##        # so the answer[0] would be 1
##        answer[0] = 1
##        for i in range(1, length):
##            
##            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
##            # Simply multiplying it with nums[i - 1] would give the product of all 
##            # elements to the left of index 'i'
##            answer[i] = nums[i - 1] * answer[i - 1]
##        
##        # R contains the product of all the elements to the right
##        # Note: for the element at index 'length - 1', there are no elements to the right,
##        # so the R would be 1
##        R = 1;
##        for i in reversed(range(length)):
##            
##            # For the index 'i', R would contain the 
##            # product of all elements to the right. We update R accordingly
##            answer[i] = answer[i] * R
##            R *= nums[i]
##        
##        return answer


##
##class Solution:
##    def productExceptSelf(self, nums: List[int]) -> List[int]:
##        n = len(nums)
##        output = [1]*(n)
##        cumProductLeft = [1]*(n+1)
##        cumProductRight = [1]*(n+1)
##        for i in range(1,n):
##            cumProductLeft[i] = cumProductLeft[i-1]*nums[i-1]
##           
##        for i in range(n-2,-1,-1):
##            cumProductRight[i] = cumProductRight[i+1]*nums[i+1]
##           
##        for i in range(n):
##            output[i]=cumProductLeft[i] * cumProductRight[i]
##            
##        return output
