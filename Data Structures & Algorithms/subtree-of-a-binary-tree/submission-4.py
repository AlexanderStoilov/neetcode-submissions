# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def areSameTree(root1, root2):
            if (not root1 and root2) or (root1 and not root2):
                return False
            if not root1 and not root2:
                return True
            if root1.val != root2.val:
                return False
            
            return areSameTree(root1.left, root2.left) and areSameTree(root1.right, root2.right)

        # find the 'subroot' starting node in 'root'
        tree1 = [root]
        while tree1:
            cur = tree1.pop()
            if not cur:
                continue
            
            if cur.val == subRoot.val:
                treesMatch = areSameTree(cur, subRoot)
                if treesMatch:
                    return True

            tree1.append(cur.left)
            tree1.append(cur.right)

        return False # 'subroot' start not found in 'root'


"""
I started by thinking I should compare subRoot with every possible subtree in root.
At first I worried this could become O(n!), but that is too pessimistic.

There can be up to n possible starting nodes in root, and comparing one candidate
with subRoot can take O(m), where m is the number of nodes in subRoot. Therefore,
the worst-case time complexity is O(n * m), not factorial.

I first thought I could search for subRoot.val in root. Then I remembered that
this is not a binary search tree, so I cannot decide to go only left or right
based on the value. However, I can still scan the entire binary tree and use
the value as a candidate filter:

    if cur.val == subRoot.val:
        # This node might be the subtree root

The values are not guaranteed to be unique, so finding one matching value is
not enough. I need to check every node with the same value.

My first attempt returned too early:

    if cur.val == subRoot.val:
        return areSameTree(cur, subRoot)

If that candidate had the correct value but the wrong structure, the function
returned False immediately and never checked later candidates.

The fix was to return only when the complete comparison succeeds:

    if cur.val == subRoot.val:
        if areSameTree(cur, subRoot):
            return True

    # Keep searching even when this candidate fails
    tree1.append(cur.left)
    tree1.append(cur.right)

The helper function compares two complete trees. It checks missing nodes,
values, and then both child pairs. The outer function searches for possible
starting nodes, while the helper verifies each candidate.

The search could also be written recursively:

    return (
        areSameTree(root, subRoot)
        or self.isSubtree(root.left, subRoot)
        or self.isSubtree(root.right, subRoot)
    )

The main edge cases are:

- multiple nodes have the same value as subRoot
- matching root values but different structure
- matching structure but different values
- subRoot is the entire root tree
- root is None or subRoot is None, if empty trees are allowed

Time complexity: O(n * m), because up to n candidates may each require
comparing up to m nodes.

Space complexity: O(h_root + h_subRoot). The iterative DFS stack uses
O(h_root) space, and the recursive tree comparison uses O(h_subRoot).
In the worst case, this becomes O(n + m).
"""        