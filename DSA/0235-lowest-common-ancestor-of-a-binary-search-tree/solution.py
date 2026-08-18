# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def fun(self,root,p,q):
        if root is None:
            return None

        if root==p or root==q:
            return root

        if p.val < root.val and q.val < root.val:
            return self.fun(root.left, p, q)

        elif p.val > root.val and q.val > root.val:
            return self.fun(root.right, p, q)

        else:
            return root
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.fun(root,p,q)