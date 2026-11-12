# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def inorder_save(self, node, arr):
        if not node:
            return
        self.inorder_save(node.left, arr)
        arr.append(node.val)
        self.inorder_save(node.right, arr)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Idea: go through elements inorder (which preserves order of values), save them into a list, return element at index k

        sorted_tree = []
        self.inorder_save(root, sorted_tree)

        return sorted_tree[k-1]

