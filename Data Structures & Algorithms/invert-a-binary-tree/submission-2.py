# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        # BFS, iteratively (cos recursively its a nigthmare :D)
        # Using deque cos its popleft O(1) and append (right side) O(1).
        # Python achieved this by using doubly linked list as the underlying structure.
        from collections import deque
        nodes = deque()
        nodes.append(root)
        while nodes:
            cur = nodes.popleft()
            if cur.left:
                nodes.append(cur.left)
            if cur.right:
                nodes.append(cur.right)
            if cur.left or cur.right: 
                cur.left, cur.right = cur.right, cur.left
            
        return root
        

        