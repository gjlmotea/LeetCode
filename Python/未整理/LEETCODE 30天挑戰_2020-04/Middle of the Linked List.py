class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow   


print(Solution().middleNode(ListNode([1, 2, 3, 4, 5])))
