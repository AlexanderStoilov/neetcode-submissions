# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isValidNode(self, node: TreeNode | None, lower: int | float, upper: int | float):
        if not node:
            return True
        if node.val <= lower or node.val >= upper:
            return False
        
        return self.isValidNode(node.left, lower, node.val) and self.isValidNode(node.right, node.val, upper)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidNode(root, float('-inf'), float('inf'))
        

"""
For Valid Binary Search Tree, I first checked each node only against its
immediate children:

    if root.left and root.left.val >= root.val:
        return False
    if root.right and root.right.val <= root.val:
        return False

That misses violations deeper in a subtree. The failing input was:

    [0, -1000, 1000, null, null, 0]

The array is level-order, so the nulls consume the two child positions of
-1000. The tree is:

        0
      /   \
  -1000   1000
           /
          0

The nested 0 is smaller than 1000, but it is still in the root's right
subtree, where it must be greater than 0.

I also tried adding this leaf check:

    if not root.left and not root.right:
        return True

That only avoids recursing from leaves. It does not change the validation
logic, so it cannot catch the deeper violation.

The fix was to pass the valid range down from every ancestor. For each node:

    if node.val <= lower or node.val >= upper:
        return False

The left subtree keeps the lower bound and uses the current node as its upper
bound. The right subtree does the opposite:

    return self.isValidNode(node.left, lower, node.val) and \
           self.isValidNode(node.right, node.val, upper)

The bounds start at negative and positive infinity. Strict comparisons reject
duplicates, and the `TreeNode | None` and `int | float` annotations match the
helper's actual inputs.

Important edge cases are an empty tree, a single-node tree, duplicate values,
and a node that violates an ancestor's bound rather than its parent's bound.

Time Complexity: O(n), because each node is visited at most once.
Space Complexity: O(h), where h is the tree height used by recursion. This is
O(log n) for a balanced tree and O(n) for a completely skewed tree.
"""