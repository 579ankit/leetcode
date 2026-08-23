class Solution(object):
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        queue=deque([root])
        res=[]
        left_to_right=True
        while queue:
            size=len(queue)
            level=[0]*size
            first=0
            last=size-1
            for _ in range(size):  
                node=queue.popleft()
                if left_to_right:
                    level[first]=node.val
                    first+=1
                else:
                    level[last]=node.val
                    last-=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
            left_to_right=not left_to_right
        return res
            