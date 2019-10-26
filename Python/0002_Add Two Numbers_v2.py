class ListNode:
    def __init__(self, x, ListNode = None):
        self.val = x
        self.next = ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        
        print(l1)
        print(l2)
        
        while True:
            sum = 0
            
            if l1 == None and l2 == None:
                break
            if l1 != None:
                sum = sum + l1.val
                l1 = l1.next
            else:
                sum = sum + l1.val
                
            if l2 != None:
                sum = sum + l2.val
                l2 = l2.next
            else:
                sum = sum + l2.val
                
                
        return l3
