# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
        if not root:
            return 0

        max_depth = 0

        level = [(root, 1)]
        while level:
            next_level = []
            for (node, depth) in level:
                max_depth = max(depth, max_depth)
                if node.left:
                    next_level.append((node.left, depth + 1))
                if node.right:
                    next_level.append((node.right, depth + 1))
            # order of processing of next level really doesnt matter cos we're going level by level, but for consistency, lets reverse it
            level = next_level[::-1] # O(N)
        
        return max_depth
