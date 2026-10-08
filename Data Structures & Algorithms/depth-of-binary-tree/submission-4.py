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

        depth = 0
        level = [root]
        while level:
            next_level = []
            depth += 1

            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
    
            level = next_level # next_level reinitialized on next iteration, so no "2 pointers -> 1 list" problem
        
        return depth
