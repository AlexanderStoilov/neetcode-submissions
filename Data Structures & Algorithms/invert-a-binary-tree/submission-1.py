# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS, iteratively

        if not root:
            return None

        stack = [root]
        while stack:
            cur = stack.pop() # by def, pops last, O(1)
            if cur.left or cur.right: # doesn't affect anything, but it's more optimal
                cur.left, cur.right = cur.right, cur.left
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return root