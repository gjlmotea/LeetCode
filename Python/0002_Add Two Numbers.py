class ListNode:
    def __init__(self, x, ListNode = None):
        self.val = x
        self.next = ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        list2 = []
        num1 = 0
        num2 = 0
        
        while True:
            if l1 != None:
                list1.append(l1.val)
                l1 = l1.next
            else:
                break;
                
        while True:
            if l2 != None:
                list2.append(l2.val)
                l2 = l2.next
            else:
                break;

        list1.reverse()
        list2.reverse()
        
        for i in list1:
            num1 = num1 * 10 + i
        for i in list2:
            num2 = num2 * 10 + i
        
        
        ans = num1 + num2
        ans = list(str(ans))
        ans.reverse()
        
        head = ListNode(0)
        l3 = head
        
        for i in ans:
            l3.next = ListNode(i)
            l3 = l3.next
        
        return head.next
