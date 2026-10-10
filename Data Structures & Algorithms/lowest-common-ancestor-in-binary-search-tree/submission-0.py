# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def findPath(self, root: TreeNode, target: TreeNode):
        path = []
        pathFound = False
        curPath = []

        def rec(cur: TreeNode):
            nonlocal pathFound, path
            if not cur or pathFound:  # pathFound presents optimization, stops any further deep dives
                return None

            curPath.append(cur)

            if target.val == cur.val:
                path = curPath[:]  # not efficient copy, but necessary
                pathFound = True
                return

            rec(cur.left)
            rec(cur.right)

            curPath.pop()

        rec(root)
        return path

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Top down paths for p and q
        pPath = self.findPath(root, p)
        qPath = self.findPath(root, q)

        # I want to find the earliest element appearing in both. But they're top-down, so reverse
        # So i'll iterate one of them, in reverse, and check if it's in the other (via set - O(1))
        pPathSet = set(pPath)

        for qAncestor in qPath[::-1]:
            if qAncestor in pPathSet:
                return qAncestor

        # no "else" case - worst case they have the root as a LCA (even if one is the root)
