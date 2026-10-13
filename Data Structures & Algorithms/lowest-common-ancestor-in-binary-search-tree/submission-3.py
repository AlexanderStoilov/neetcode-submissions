# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #         At any current node:
        # If both p and q are smaller, their LCA must be in the left subtree.
        # If both are larger, their LCA must be in the right subtree.
        # Otherwise, the current node is the split point—or it is one of the targets—and therefore is the LCA.

            if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
                return root
            elif p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)


"""
I initially treated this as a general binary-tree problem. My first idea was to
find the ancestor path for p and q, then find the deepest node appearing in
both paths.

I first tried to build the path while unwinding recursion. The idea was roughly:

    def findAndGetAncestorChainBottomUp(
        self, chain, onChain=False, cur, target
    ):
        ...

There were several problems in that draft:

- Python does not allow required parameters after a default parameter.
- I accidentally searched cur.left twice instead of searching cur.right.
- onChain is a boolean passed into each recursive call. Assigning
  onChain = True in one call does not update the other calls.
- Returning from the call that finds the target does not automatically make
  every parent call stop. Each parent must inspect the child result and
  propagate success.

The next idea was to maintain the current path while doing DFS. I initially
appended children directly:

    path.append(cur.left)
    rec(cur.left)
    path.pop()

This was awkward because the path should represent the route to cur, so the
current node itself should be appended before searching its children.

I also ignored the return values from rec. A return only exits the current
function call. It does not force the caller to return unless the caller uses
that result.

I eventually got a working general-binary-tree solution by keeping a
curPath, copying it when the target was found, and using pathFound to stop
further searches:

    class Solution:
        def findPath(self, root, target):
            path = []
            pathFound = False
            curPath = []

            def rec(cur):
                nonlocal pathFound, path

                if not cur or pathFound:
                    return None

                curPath.append(cur)

                if target.val == cur.val:
                    path = curPath[:]
                    pathFound = True
                    return

                rec(cur.left)
                rec(cur.right)

                curPath.pop()

            rec(root)
            return path

        def lowestCommonAncestor(self, root, p, q):
            pPath = self.findPath(root, p)
            qPath = self.findPath(root, q)

            pPathSet = set(pPath)

            for qAncestor in qPath[::-1]:
                if qAncestor in pPathSet:
                    return qAncestor

This works, but it solves a more general problem than necessary. It would work
for an ordinary binary tree too, not just a binary search tree.

The nonlocal detail was another useful Python lesson.

This does not need nonlocal:

    path.append(cur)

It mutates the existing list object.

These do need nonlocal:

    path = curPath[:]
    pathFound = True

They reassign the variable names. Without nonlocal, Python creates local
variables inside rec and the outer path/pathFound do not change.

The copy is also necessary. If I wrote path = curPath, both names would refer to
the same list, and later backtracking pop operations would modify the saved
path.

The same path search can be written more cleanly by using a boolean return
value instead of pathFound:

    def findPath(self, root, target):
        path = []

        def rec(cur):
            if cur is None:
                return False

            path.append(cur)

            if cur is target:
                return True

            if rec(cur.left) or rec(cur.right):
                return True

            path.pop()
            return False

        rec(root)
        return path

Here, a successful recursive call returns True through every ancestor. The
path is only popped when the current branch fails.

Using cur is target is more precise than comparing values, because the target
is a particular node. Comparing target.val is only safe when values are known
to be unique. The __repr__ method I added was fine for debugging and did not
change the tree logic.

Then I realized the important detail: this problem is specifically about a
binary search tree. The BST ordering means I do not need to construct either
path.

At any current node:

- If p and q are both smaller, their LCA must be in the left subtree.
- If p and q are both larger, their LCA must be in the right subtree.
- Otherwise, the current node is between them, or it is p or q itself, so it is
  the LCA.

My first BST attempt was too restrictive:

    if p.val < root.val < q.val:
        return root
    elif q.val < root.val:
        return self.lowestCommonAncestor(root.left, p, q)
    else:
        return self.lowestCommonAncestor(root.right, p, q)

It assumed p and q were always ordered as p < q and did not account for the LCA
being one of the targets.

I then tried inclusive comparisons, but initially only handled one ordering:

    if p.val <= root.val <= q.val:
        return root

That still failed when q was smaller than p. The corrected version considered
both orders:

    if (
        p.val <= root.val <= q.val
        or q.val <= root.val <= p.val
    ):
        return root

    if p.val < root.val and q.val < root.val:
        return self.lowestCommonAncestor(root.left, p, q)

    return self.lowestCommonAncestor(root.right, p, q)

This passed.

A clearer equivalent is to handle the two same-side cases first and let the
remaining case be the split point:

    class Solution:
        def lowestCommonAncestor(self, root, p, q):
            if p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)

            if p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)

            return root

The recursive returns are the part I was initially overthinking:

    return self.lowestCommonAncestor(root.left, p, q)

The current call waits for the recursive call to return. Once the deeper call
finds the LCA, each parent returns that same node. The result naturally
propagates while the stack unwinds.

The final return root handles all remaining cases:

- p and q are on opposite sides
- root is p
- root is q
- p and q are the same node, if that is allowed

The problem guarantees that p and q exist in the tree, so the recursive search
will not reach None. A defensive implementation could still handle root is
None and return None.

The path-based solution has O(n) time because it may search the tree twice and
O(h) auxiliary space, which is O(n) for a skewed tree.

The final BST solution has O(h) time because it follows only one root-to-leaf
path. It uses O(h) recursion-stack space. For a balanced BST, h is O(log n);
for a completely skewed BST, h is O(n).

An iterative version would preserve the O(h) time and reduce extra space to
O(1), but the recursive version is already correct.
"""