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
            if root.val<self.prev.val:
                if self.galat==0:
                    self.g1first=self.prev
                    self.g1second=root
                    self.galat+=1
                else:
                    self.g2first=self.prev
                    self.g2second=root
                    self.galat+=1
            self.prev=root
        self.fun(root.right)

    def recoverTree(self, root):
        self.prev=None
        self.galat=0
        self.g1first=None
        self.g1second=None
        self.g2first=None
        self.g2second=None
        self.fun(root)
        if self.galat==1:
            self.g1first.val,self.g1second.val=self.g1second.val,self.g1first.val
        else:
            self.g1first.val,self.g2second.val=self.g2second.val,self.g1first.val