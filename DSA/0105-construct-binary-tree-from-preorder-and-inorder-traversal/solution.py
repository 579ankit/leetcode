class Solution:
    def buildTree(self, preorder, inorder):
        # Store the index of every value in inorder
        pos = {}
        for i in range(len(inorder)):
            pos[inorder[i]] = i
        idx = [0]
        def build(low, high):
            if low > high:
                return None
            # First element in preorder is the root
            root = TreeNode(preorder[idx[0]])
            idx[0] += 1
            # Find root position in inorder in O(1)
            mid = pos[root.val]
            # Build left subtree
            root.left = build(low, mid - 1)
            # Build right subtree
            root.right = build(mid + 1, high)
            return root
        return build(0, len(inorder) - 1)