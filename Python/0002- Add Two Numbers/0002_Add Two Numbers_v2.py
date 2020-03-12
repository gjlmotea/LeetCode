class ListNode:
    def __init__(self, x, ListNode = None):
        self.val = x
        self.next = ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        l3 = ListNode
        head = l3
        
        while True:
            if l1 == None and l2 == None and carry == 0:
                break

            sum = 0
            sum = sum + carry
            
            if l1 != None:
                sum = sum + l1.val
                l1 = l1.next
                
            if l2 != None:
                sum = sum + l2.val
                l2 = l2.next
            
            if(sum > 9):
                carry = 1
                sum = sum - 10
            else:
                carry = 0
            
            l3.next = ListNode(sum)
            l3 = l3.next
            
        return head.next
