class Solution:
    def isHappy(self, n: int) -> bool:
        unhappy = set()
        sum = 0
        while n not in unhappy:
            unhappy.add(sum)
            sum = 0
            for i in str(n):
                #print("====",int(i)**2)
                sum = sum + int(i)**2
            #print(sum)
            n = sum
        if n == 1:
            return True
        else:
            return False
        
print(Solution().isHappy(20))
