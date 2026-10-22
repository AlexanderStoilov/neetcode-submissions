# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            level_len = len(queue)
            cur_level_vals = []
            for _ in range(level_len):
                node = queue.popleft()
                cur_level_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(cur_level_vals)

        return result


        