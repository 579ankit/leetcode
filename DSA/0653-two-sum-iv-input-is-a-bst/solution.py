class Solution(object):
    def findTarget(self, root, k):
        if root is None:
            return False
        left_stack = []
        right_stack = []
        # Put all left nodes into left_stack
        def push_left(node):
            while node:
                left_stack.append(node)
                node = node.left
        # Put all right nodes into right_stack
        def push_right(node):
            while node:
                right_stack.append(node)
                node = node.right
        push_left(root)
        push_right(root)
        while left_stack and right_stack:
            left_node = left_stack[-1]
            right_node = right_stack[-1]
            # Same node
            if left_node == right_node:
                return False
            left_val = left_node.val
            right_val = right_node.val
            current_sum = left_val + right_val
            if current_sum == k:
                return True
            elif current_sum < k:
                # Move left pointer forward
                node = left_stack.pop()
                push_left(node.right)
            else:
                # Move right pointer backward
                node = right_stack.pop()
                push_right(node.left)
        return False