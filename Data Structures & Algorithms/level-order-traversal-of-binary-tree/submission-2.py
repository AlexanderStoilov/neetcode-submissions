# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        level = [root]
        nodes = []

        while level:
            cur_level_vals = []
            next_level = []
            for node in level:
                cur_level_vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            nodes.append(cur_level_vals)
            level = next_level

        return nodes

                
