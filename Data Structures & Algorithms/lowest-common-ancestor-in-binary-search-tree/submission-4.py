# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # iterative version of prev solution
        low = min(p.val, q.val)
        high = max(p.val, q.val)

        cur = root
        while cur:
            if low <= cur.val <= high:
                return cur
            elif low < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        

"""
I initially solved this as a general binary-tree problem by finding the path
from the root to p and q, then finding their deepest common node.

That solution worked, but it ignored the most important fact: this is a binary
search tree. The ordering gives a direct way to navigate without building
paths.

At any current node:

- If both p and q are smaller, the LCA must be in the left subtree.
- If both are larger, the LCA must be in the right subtree.
- Otherwise, the current node is between them or is one of the targets, so it
  is the LCA.

I first wrote the recursive version. The important recursion detail was:

    return self.lowestCommonAncestor(root.left, p, q)

The recursive call finds the answer, and every parent returns that same answer
while the stack unwinds. A recursive call without return would lose the result.

I then converted the same logic to iterative DFS using cur:

    cur = root

    while cur:
        if p.val < cur.val and q.val < cur.val:
            cur = cur.left
        elif p.val > cur.val and q.val > cur.val:
            cur = cur.right
        else:
            return cur

My first interval-based attempt was:

    if p.val < cur.val < q.val:
        return cur
    elif q.val < cur.val:
        cur = cur.left
    else:
        cur = cur.right

This was wrong because it assumed p.val was smaller than q.val. The inputs can
come in either order. It also needed inclusive comparisons because the LCA can
be p or q itself.

The corrected version handled both orderings:

    if (
        p.val <= cur.val <= q.val
        or q.val <= cur.val <= p.val
    ):
        return cur
    elif max(p.val, q.val) < cur.val:
        cur = cur.left
    else:
        cur = cur.right

The interval condition identifies the split point, including cases where cur is
one of the target nodes. If cur is greater than both target values, both targets
must be in the left subtree. Otherwise, after the interval check, both targets
must be greater than cur, so moving right is correct.

A slightly cleaner equivalent computes the bounds once:

    class Solution:
        def lowestCommonAncestor(self, root, p, q):
            low = min(p.val, q.val)
            high = max(p.val, q.val)

            cur = root

            while cur:
                if low <= cur.val <= high:
                    return cur

                if high < cur.val:
                    cur = cur.left
                else:
                    cur = cur.right

            return None

The main edge cases are:

- p and q are on opposite sides of the current node
- p is the ancestor of q
- q is the ancestor of p
- the root itself is the LCA
- p and q arrive in either order
- the LCA is exactly p or q

The problem guarantees that both nodes exist in the tree, so the final return
None is only defensive.

Time complexity: O(h), because the algorithm follows only one path from the
root instead of searching the entire tree.

Space complexity: O(1) extra space, because the iterative version only keeps
the current node. For a balanced BST, h is O(log n); for a completely skewed
BST, h is O(n).
"""