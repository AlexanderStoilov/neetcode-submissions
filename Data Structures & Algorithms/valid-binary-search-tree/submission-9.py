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

"""
This is the iterative follow-up to the recursive bounds solution. The main
BST idea stayed the same: every node needs to be checked against the bounds
provided by its ancestors.

Instead of letting recursion carry those bounds, I stored each pending node
with its lower and upper limits:

    (node, lower, upper)

My first deque initialization was:

    queue = deque((root, float('-inf'), float('inf')))

I originally thought this represented one three-value item. However, deque
takes an iterable and adds each item from it, so this creates:

    deque([root, float('-inf'), float('inf')])

When I called `queue.pop()`, it returned only `float('inf')`. That caused this
unpacking to fail:

    cur, lower, upper = queue.pop()

The corrected version wraps the triple inside an outer container:

    queue = deque([(root, float('-inf'), float('inf'))])

Now the deque contains one item, and that item is the complete triple.

The distinction is:

    deque([el1, el2, el3])              # three separate deque items
    deque([(root, lower, upper)])       # one deque item containing a triple

The final loop pops one complete record at a time and validates it:

    cur, lower, upper = queue.pop()

    if not self.isValidNode(cur, lower, upper):
        return False

Children are added with the bounds they inherit from their parent:

    if cur.left:
        queue.appendleft((cur.left, lower, cur.val))
    if cur.right:
        queue.appendleft((cur.right, cur.val, upper))

The iterative version passes while preserving the same strict-bound logic,
so duplicates and values that violate an ancestor's constraint are rejected.
An empty tree still returns True.

Time Complexity: O(n), because each node is processed once.
Space Complexity: O(w), where w is the maximum number of pending nodes in the
deque. In the worst case, this is O(n).
"""