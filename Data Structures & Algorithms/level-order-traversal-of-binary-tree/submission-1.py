# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # first idea - bfs, by levels
        if not root:
            return []

        # from collections import deque - looks like we dont need it
        level = [root]
        nodes = []

        while level:
            level_vals = []
            for node in level:
                level_vals.append(node.val)
            nodes.append(level_vals)

            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            level = next_level # pointer copy ok, cos on next iter we do "next_level = []" so we clean next_level to not be related to level any more

        return nodes
