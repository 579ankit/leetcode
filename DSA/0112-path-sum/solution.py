# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def fun(self,root,s,targetSum):
        if root is None:
            return False
        s+=root.val
        if root.left is None and root.right is None:
            if s==targetSum:
                return True
        left=self.fun(root.left,s,targetSum)
        right=self.fun(root.right,s,targetSum)

        return left or right

    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        return self.fun(root,0,targetSum)