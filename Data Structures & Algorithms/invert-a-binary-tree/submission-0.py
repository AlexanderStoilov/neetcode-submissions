# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Divide and Conquer Recursive approach

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def flip(node):
            if not node.left and not node.right:
                return
            else:
                node.left, node.right = node.right, node.left
        
        def divide(node):
            if not node:
                return None
            divide(node.left)
            divide(node.right)
            flip(node)

        divide(root)
        return root

# Flip the tree in place. Every node object stays where it is.
# flip only swaps that node's left and right links.
# divide walks down to those same objects and does not return them.
# The parent already holds the child, so there is nothing to assign
# back. node.left = divide(node.left) would store None and drop the child.
# The original root is still the root after those swaps, so return root.

"""
Invert Binary Tree. One recursive walk that flips the tree in place.

divide goes left, then right, then flip swaps that node's two child links.
A leaf has nothing to swap, so flip returns. A node with one child still
swaps, so the child moves to the other side. An empty root never reaches
flip: divide returns, and we return that same empty root.

I thought the helper had to hand the subtrees back up:

    node.left = divide(node.left)
    node.right = divide(node.right)
    node = flip(node)
    return node

and that the outer function would return divide(root). It does not.
The swap is already on the object. The parent still points at that 
same object, and the original root is still the root, so we return root.

I first called the stack O(N) because every parent would sit on a divide
stack and again on a flip stack, O(2N). The stack only holds the path
from the root to the node we are on. That length is the height H. flip
is one extra frame, and it is gone as soon as flip returns. The left
path is gone before the right path starts.

Time Complexity: O(N). Each node is visited once, and the swap is O(1).
Space Complexity: O(H). Balanced tree O(log N). Straight line O(N).
"""