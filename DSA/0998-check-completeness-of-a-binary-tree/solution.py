class Solution(object):
    def isCompleteTree(self, root):
        if root is None:
            return True
        q = deque([root])
        seen_none = False
        while q:
            node = q.popleft()
            if node is None:
                seen_none = True
            else:
                if seen_none:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True