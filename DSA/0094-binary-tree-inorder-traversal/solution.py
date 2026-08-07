# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def fun(self, node, res):
        if node is None:
            return

        self.fun(node.left, res)
        res.append(node.val)
        self.fun(node.right, res)

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        self.fun(root, res)
        return res