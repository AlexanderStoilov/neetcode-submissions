# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #         At any current node:
        # If both p and q are smaller, their LCA must be in the left subtree.
        # If both are larger, their LCA must be in the right subtree.
        # Otherwise, the current node is the split point—or it is one of the targets—and therefore is the LCA.

            if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
                return root
            elif p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)