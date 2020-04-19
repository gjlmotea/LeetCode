class ListNode:
    def __init__(self, x, ListNode = None):
        self.val = x
        self.next = ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        list2 = []
        
        while l1:
            list1.append(l1.val)
            l1 = l1.next
                
        while l2:
            list2.append(l2.val)
            l2 = l2.next
            
        list1.reverse()
        list2.reverse()
        
        num1 = 0
        num2 = 0
        for i in list1:
            num1 = num1 * 10 + i
        for i in list2:
            num2 = num2 * 10 + i
        
        ans = num1 + num2
        ans = list(str(ans))
        ans.reverse()

        head = ListNode
        l3 = head

        for i in ans:
            l3.next = ListNode(i)
            l3 = l3.next
        return head.next


## Test
def display(listnode):
    while listnode:
        print(listnode.val, end = '-> ')
        listnode = listnode.next

        
l1 = ListNode(2, ListNode(4, ListNode(3, None)))
l2 = ListNode(5, ListNode(6, ListNode(4, None)))
print(display(l1))
print(display(l2))

#l1 = ListNode(8, ListNode(1, None))

#l2 = ListNode(0, None)
l3 = Solution().addTwoNumbers(l1, l2)
display(l3)
