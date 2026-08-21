class Solution(object):

    def fun(self, root):
        if root is None:
            return 0
        left = self.fun(root.left)
        right = self.fun(root.right)
        s = left + right
        self.res = max(self.res, s)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root):
        self.res = 0
        self.fun(root)
        return self.res