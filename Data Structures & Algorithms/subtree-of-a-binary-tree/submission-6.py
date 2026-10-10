# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Serialization and Pattern Matching
        ## convert both trees into a ordered traversal of choice (inorder, preorder, postorder) and compare subarray in array

        def to_preorder_with_None(node):
            def rec(node):
                if not node:
                    arr.append(node)
                    return
                arr.append(node.val)
                rec(node.left)
                rec(node.right)

            arr = []
            rec(node)
            return arr

        def pattern_matches(big: list[int], i: int, small: list[int]):
            j = 0
            while j < len(small):
                if i >= len(big):  # ran out of big while traversing
                    return False
                if big[i] != small[j]:  # chars dont match
                    return False
                i += 1
                j += 1
            return True

        tree1 = to_preorder_with_None(root)
        tree2 = to_preorder_with_None(subRoot)

        for i in range(len(tree1)):
            if tree1[i] == tree2[0] and pattern_matches(tree1, i, tree2):
                return True
        return False


"""
This problem started with the same basic idea as Same Tree:

1. Find possible starting nodes in root.
2. Whenever a node could be the root of subRoot, compare the two trees completely.

I first thought that checking every node and then checking the whole subtree below
it might be factorial. That was too pessimistic. If root has n nodes and subRoot
has m nodes, there can be up to n candidate nodes, and each comparison can cost
O(m). The worst-case time is O(n * m), not O(n!).

I also realized that this is not a binary search tree. That means I cannot use
value ordering to decide whether to go left or right. However, I can still scan
the entire binary tree and use subRoot.val as a cheap candidate filter. Values
are not guaranteed to be unique, so every matching value must be checked.

My first implementation was:

    class Solution:
        def isSubtree(self, root, subRoot):
            def isSubtreeRec(root1, root2):
                if (not root1 and root2) or (root1 and not root2):
                    return False
                if not root1 and not root2:
                    return True
                if root1.val != root2.val:
                    return False

                return (
                    isSubtreeRec(root1.left, root2.left)
                    and isSubtreeRec(root1.right, root2.right)
                )

            if not root:
                if not subRoot:
                    return True
                return False

            if not subRoot:
                return True

            tree1 = [root]

            while tree1:
                cur = tree1.pop()

                if not cur:
                    continue

                if cur.val == subRoot.val:
                    return isSubtreeRec(cur, subRoot)
                else:
                    tree1.append(cur.left)
                    tree1.append(cur.right)

            return False

This failed because of duplicate values. If the first node with the same value as
subRoot was not the correct subtree, the function immediately returned False and
never checked later candidates.

The else branch also meant that children were only added when the current value
did not match subRoot.val. A matching candidate still needed to have its children
added if the full comparison failed.

The corrected iterative DFS was:

    class Solution:
        def isSubtree(self, root, subRoot):
            def areSameTree(root1, root2):
                if (not root1 and root2) or (root1 and not root2):
                    return False
                if not root1 and not root2:
                    return True
                if root1.val != root2.val:
                    return False

                return (
                    areSameTree(root1.left, root2.left)
                    and areSameTree(root1.right, root2.right)
                )

            if not root:
                if not subRoot:
                    return True
                return False

            if not subRoot:
                return True

            tree1 = [root]

            while tree1:
                cur = tree1.pop()

                if not cur:
                    continue

                if cur.val == subRoot.val:
                    matches = areSameTree(cur, subRoot)

                    if matches:
                        return True

                # Always continue searching after a failed candidate.
                tree1.append(cur.left)
                tree1.append(cur.right)

            return False

The important change was returning True only when the complete tree comparison
succeeded. A failed candidate did not end the search.

The same idea can be written recursively. At each node, first ask whether the
trees match starting here. If they do not, search the left and right children:

    class Solution:
        def areSameTree(self, a, b):
            if a is None or b is None:
                return a is b

            return (
                a.val == b.val
                and self.areSameTree(a.left, b.left)
                and self.areSameTree(a.right, b.right)
            )

        def isSubtree(self, root, subRoot):
            if subRoot is None:
                return True

            if root is None:
                return False

            return (
                self.areSameTree(root, subRoot)
                or self.isSubtree(root.left, subRoot)
                or self.isSubtree(root.right, subRoot)
            )

This version makes the two jobs very clear:

- areSameTree checks whether two complete trees are equal.
- isSubtree searches for the possible starting node.

Both of these candidate-search solutions have worst-case time complexity
O(n * m), because the same subRoot comparison may be repeated for many nodes in
root.

I then tried serialization and pattern matching. My first idea was to serialize
both trees using inorder traversal and search for the smaller array inside the
larger array.

For the example:

    root    = [1, 2, 3, 4, 5, None, None, 6]
    subRoot = [2, 4, 5]

the inorder value arrays are:

    root:    [6, 4, 2, 5, 1, 3]
    subRoot: [4, 2, 5]

The subRoot values appear contiguously, but the trees are not equal because node
4 in root has an extra child 6.

This showed that a traversal containing only values does not preserve enough
information about the tree shape. The sequence does not tell us that 4 should
have no left child.

Also, simply checking the nodes after the pattern would not be correct. A valid
subtree can be followed by other values belonging to its parent or neighboring
subtrees. The pattern itself needs to include the subtree boundaries.

The fix was to include None markers for missing children. Preorder is a good
choice:

    root serialization:
    [1, 2, 4, 6, None, None, None, 5, None, None, 3, None, None]

    subRoot serialization:
    [2, 4, None, None, 5, None, None]

After matching 2 and 4, the pattern expects None, but root contains 6. The
extra child is therefore detected.

The None markers are the important part. Preorder and postorder with explicit
None markers preserve the values and the tree shape. Plain preorder or
postorder values alone are not enough.

Inorder is especially unsuitable for this substring approach. Even inorder
with None markers is not a reliable unique encoding of an ordered binary tree.
For example, these two trees can produce the same inorder-with-None sequence:

    Tree A: root 1 with left child 2
    Tree B: root 2 with right child 1

Both serialize to:

    [None, 2, None, 1, None]

So for this problem, preorder or postorder with missing-child markers is the
safer representation.

My final serialization solution was:

    class Solution:
        def isSubtree(self, root, subRoot):
            if subRoot is None:
                return True

            if root is None:
                return False

            def to_preorder_with_none(node):
                result = []

                def dfs(node):
                    if node is None:
                        result.append(None)
                        return

                    result.append(node.val)
                    dfs(node.left)
                    dfs(node.right)

                dfs(node)
                return result

            def pattern_matches(big, start, small):
                j = 0

                while j < len(small):
                    if start >= len(big):
                        return False

                    if big[start] != small[j]:
                        return False

                    start += 1
                    j += 1

                return True

            tree1 = to_preorder_with_none(root)
            tree2 = to_preorder_with_none(subRoot)

            for i in range(len(tree1) - len(tree2) + 1):
                if (
                    tree1[i] == tree2[0]
                    and pattern_matches(tree1, i, tree2)
                ):
                    return True

            return False

The first version of to_inorder also had a small separate bug: it defined rec
but did not call rec(node) or return arr. That was fixed in the next version.

The local j variable does not need to be passed into pattern_matches. It should
start at zero for each possible starting index. However, j is still needed
inside the function to track the current position in the smaller pattern.

I also tried to optimize the outer loop by returning the mismatch index:

    return False, i

and then doing:

    i = i_to_move_to

That optimization was incorrect. A mismatch can happen after a prefix that
contains the beginning of another valid match.

For example:

    big:   [1, 1, 1, 2]
    small: [1, 1, 2]

The attempt starting at index 0 matches the first two values, then fails at
index 2. Jumping directly to index 2 skips the valid match that starts at
index 1.

For simple pattern matching, the safe move is to try the next starting position:

    start += 1

The final version scans every possible starting position, so it does not skip
overlapping matches. A smarter jump requires KMP's prefix/LPS table. My current
solution is serialization plus naive pattern matching, not KMP yet.

Final complexity for the serialization solution:

- Serializing both trees takes O(n + m) time.
- Naive pattern matching takes O(n * m) time in the worst case.
- Total time complexity is O(n * m).
- The serialized arrays use O(n + m) space.
- Recursive serialization uses O(h) call-stack space, which is dominated by
  the arrays in the overall space complexity.

A true KMP version would reduce the matching time and give O(n + m) total time,
while still using O(n + m) space for the serialized arrays and prefix table.
"""


# s = Solution()

# # root=[1,2,3,4,5,null,null,6]
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.left.left.left = TreeNode(6)

# # subRoot=[2,4,5]
# subRoot = TreeNode(2)
# subRoot.left = TreeNode(4)
# subRoot.right = TreeNode(5)

# res = s.isSubtree(root, subRoot)
# print(res)
