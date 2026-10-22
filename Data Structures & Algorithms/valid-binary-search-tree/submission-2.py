# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isValidNode(self, node: TreeNode, lower: int, upper: int):
        if not node:
            return True
        if node.val <= lower or node.val >= upper:
            return False
        
        return self.isValidNode(node.left, lower, node.val) and self.isValidNode(node.right, node.val, upper)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidNode(root, float('-inf'), float('inf'))
        