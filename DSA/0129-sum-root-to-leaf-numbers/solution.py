# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def fun(self,root,s):
        if root is None:
            return False
        s=s*10+root.val
        if root.left is None and root.right is None:
            return s
        left=self.fun(root.left,s)
        right=self.fun(root.right,s)

        return left+right
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.fun(root,0)
