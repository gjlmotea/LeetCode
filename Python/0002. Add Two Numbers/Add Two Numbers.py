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
        print("num1 :", num1)
        print("num2 :", num2)        
        
        ans = num1 + num2
        print("ans: ", ans)
        ans = list(str(ans))
        ans.reverse()
                
        head = ListNode
        l3 = head
        
        for i in ans:
            print(i)
            l3.next = ListNode(i)
            l3 = l3.next
        
        return head.next


## Test
'''
#l1 = ListNode(2, ListNode(4, ListNode(3, None)))
#l2 = ListNode(5, ListNode(6, ListNode(4, None)))
l1 = ListNode(8, ListNode(1, None))
l2 = ListNode(0, None)
print(Solution.addTwoNumbers(object(),l1, l2))
'''
