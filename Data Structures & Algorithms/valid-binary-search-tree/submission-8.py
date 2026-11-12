# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isValidNode(self, node, lower, upper):
        if not (lower < node.val < upper):
            return False
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([( root, float('-inf'), float('inf') )])
        while queue:
            cur, lower, upper = queue.pop()

            if not self.isValidNode(cur, lower, upper):
                return False

            if cur.left:
                queue.appendleft((cur.left, lower, cur.val))
            if cur.right:
                queue.appendleft((cur.right, cur.val, upper))
        
        return True

            
