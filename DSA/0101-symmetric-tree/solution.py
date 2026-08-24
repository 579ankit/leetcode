# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def fun(self,p,q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val!=q.val:
            return False
        r1=self.fun(p.left,q.right)
        r2=self.fun(p.right,q.left)
        if r1 and r2:
            return True
        else:
            return False
        
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.fun(root.left,root.right)
