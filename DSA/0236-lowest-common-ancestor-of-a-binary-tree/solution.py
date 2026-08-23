class Solution(object):
    def fun(self,root,p,q):
        if root is None:
            return 0
        left_part=self.fun(root.left,p,q)
        right_part=self.fun(root.right,p,q)
        curr=0
        if root==p or root==q:
            curr=1
        total=left_part+curr+right_part
        if total==2 and self.ans is None:
            self.ans=root
        return total
        
    def lowestCommonAncestor(self, root, p, q):
        self.ans=None
        self.fun(root,p,q)
        return self.ans