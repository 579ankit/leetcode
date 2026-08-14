class Solution(object):
    def fun(self, node, p, q):
        if node is None:
            return 0
        left = self.fun(node.left, p, q)
        right = self.fun(node.right, p, q)
        current=0
        if node == p or node == q:
            current = 1
        total = left + right + current
        if total == 2 and self.ans is None:
            self.ans = node
        return total
        
    def lowestCommonAncestor(self, root, p, q):
        self.ans = None
        self.fun(root, p, q)
        return self.ans