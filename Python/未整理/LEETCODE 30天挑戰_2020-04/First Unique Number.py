from typing import List
import collections
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.deque = collections.deque()
        self.lookup = {}
        for num in nums:
            self.add(num)
            self.remove(num)

    def showFirstUnique(self) -> int:
        if len(self.deque) == 0:
            return -1
        while len(self.deque) > 0 and self.deque[0] in self.lookup and self.lookup[self.deque[0]] >= 2:
            self.deque.popleft()
        if len(self.deque) == 0:
            return -1
        return self.deque[0]

    def add(self, value: int) -> None:
        if value in self.lookup:
            self.lookup[value] += 1
        else:
            self.lookup[value] = 1

        self.deque.append(value)
        
firstUnique = FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique();
firstUnique.add(7);
firstUnique.add(3);
firstUnique.add(3);
firstUnique.add(7);
firstUnique.add(17);
print(firstUnique.showFirstUnique())


##用List超時
##from typing import List
##from collections import deque
##class FirstUnique:
##    def __init__(self, nums: List[int]):
##        self.nums = deque(nums)
##        self.numDict = {}
##        for num in self.nums:
##            if num not in self.numDict:
##                self.numDict[num] = 1
##            else:
##                self.numDict[num] += 1
##
##    def showFirstUnique(self) -> int:
##        if len(self.nums) == 0:
##            return -1
##        for num in self.nums:
##            if self.numDict[num] == 1:
##                return num
##        else:
##            return -1
##
##    def add(self, value: int) -> None:
##        self.nums.append(value)
##        if value not in self.numDict:
##            self.numDict[value] = 1
##        else:
##            self.numDict[value] += 1
##        


##class FirstUnique:
##
##    def __init__(self, nums: List[int]):
##        self.d = collections.OrderedDict()
##        for num in nums:
##            self.d[num] = self.d.get(num, 0) + 1
##        self.removed = set()
##        for key in list(self.d.keys()):
##            if self.d[key] > 1:
##                self.removed.add(key)
##                self.d.pop(key)
##        # print(self.d)
##        # print(next(iter(self.d)))
##
##    def showFirstUnique(self) -> int:
##        return next(iter(self.d)) if self.d else -1
##        
##
##    def add(self, value: int) -> None:
##        if value not in self.removed:
##            if value in self.d:
##                self.d.pop(value)
##                self.removed.add(value)
##            else:
##                self.d[value] = 1

##
##from collections import Counter, deque
##
##class FirstUnique:
##
##    def __init__(self, nums: List[int]):
##        self.c = Counter(nums)
##        self.d = deque(nums)
##
##    def showFirstUnique(self) -> int:
##        while self.d and self.c[self.d[0]] != 1: 
##            self.d.popleft()
##        return self.d[0] if self.d else -1
##            
##
##    def add(self, value: int) -> None:
##        self.c[value] += 1
##        self.d.append(value)
