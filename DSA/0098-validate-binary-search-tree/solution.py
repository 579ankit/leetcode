# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def fun(self,root):
        if root is None:
            return 
        self.fun(root.left)
        if self.prev is None:
            self.prev=root
        else:
            if root.val<=self.prev.val:
                self.ans=False
            self.prev=root
        self.fun(root.right)

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.prev=None
        self.ans=True
        self.fun(root)
        return self.ans