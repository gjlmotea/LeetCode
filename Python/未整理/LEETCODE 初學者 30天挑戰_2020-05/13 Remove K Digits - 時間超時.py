class Solution(object):
    def removeKdigits(self, num, k):
        st, required = [], k
        for x in num:
            while required and st and st[-1] > x:
                st.pop()
                required = required-1
            st.append(x)
        result = "".join(st[0:len(num)-k]).lstrip("0")
        return result if len(result) else "0"
        
print(Solution().removeKdigits("1432219",3))
print(Solution().removeKdigits("1020000111",3))
#print(Solution().removeKdigits("10",2))

##暴力法 超時
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'
        while k > 0:
            #print("k: ",k)
            for i in range(k):
                if '0' in str(num)[0:k]:
                    if len(str(num)) > 1:
                        num = int(str(num)[1:])
                    else:
                        return '0'
                else:
                    num = self.popOne(num)
                k -= 1
        return str(int(num))
    
    def popOne(self, num):
        Min = num
        for i in range(len(str(num))):
            popOne = ""
            popOne = str(num)[:i] + str(num)[i+1:]
            #print("popOne:", popOne)
            Min = min(int(Min), int(popOne))
        #print("Min", Min)
        return Min
