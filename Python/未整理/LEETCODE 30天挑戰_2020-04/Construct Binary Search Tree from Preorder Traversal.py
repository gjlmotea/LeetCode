from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
      root = TreeNode(preorder[0])
      stack = [root]
      for i in preorder[1:]:
         i = TreeNode(i)
         if i.val<stack[-1].val:
            stack[-1].left = i
            stack.append(i)
         else:
            while stack and stack[-1].val<i.val:
               last = stack.pop(-1)
            last.right = i
            stack.append(i)
      return root

print(Solution().bstFromPreorder([8,5,1,7,10,12]))
