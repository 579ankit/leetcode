# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def fun(self,root,s,targetSum,diary,res):
        if root is None:
            return None
        s+=root.val
        diary.append(root.val)
        if root.left is None and root.right is None:
            if s==targetSum:
                res.append(diary[:])
        else:
            self.fun(root.left,s,targetSum,diary,res)
            self.fun(root.right,s,targetSum,diary,res)
        diary.pop()
    
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res=[]
        diary=[]
        self.fun(root,0,targetSum,diary,res)
        return res