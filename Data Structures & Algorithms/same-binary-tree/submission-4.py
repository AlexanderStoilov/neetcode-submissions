# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS iterative
        pStack = [p]
        qStack = [q]

        while pStack and qStack:
            pCur = pStack.pop()
            qCur = qStack.pop()

            if (not pCur and not qCur):
                continue

            if (pCur and not qCur) or (qCur and not pCur) or (pCur.val != qCur.val):
                return False
            
            pStack.append(pCur.left)
            pStack.append(pCur.right)
            qStack.append(qCur.left)
            qStack.append(qCur.right)

        if (pStack and not qStack) or (qStack and not pStack):
            return False

        return True


"""
I started with recursive DFS. For each pair of nodes, I checked:

- both nodes are None: the subtrees match
- only one is None: the structures differ
- values differ: the trees differ
- otherwise, recursively compare both child pairs

That solution was straightforward and passed.

I then tried iterative DFS with two stacks. The important invariant is that both stacks contain corresponding nodes in the same order.

My first draft forgot to add the children after comparing the current nodes. It therefore only compared the roots. For example, two roots with equal values but different children would incorrectly return True.

When pushing child nodes, I also needed to handle pairs of None values. If both current nodes are None, I must continue before accessing `.val`. Otherwise, the code reaches:

    pCur.val

and raises an error.

I experimented with not pushing None children. That can work, but then every left and right child must be checked separately.

A simpler iterative solution is to keep pairs of corresponding nodes in one stack:

    stack = [(p, q)]

    while stack:
        pCur, qCur = stack.pop()

        if pCur is None and qCur is None:
            continue

        if pCur is None or qCur is None:
            return False

        if pCur.val != qCur.val:
            return False

        stack.append((pCur.left, qCur.left))
        stack.append((pCur.right, qCur.right))

    return True


While debugging, I also learned that __str__ and __repr__ must return a string. Returning an integer directly from either method causes an error, so the value must be converted with str(value) or an f-string.

The main edge cases are:

- both roots are None
- only one root is None
- equal values but different structure
- equal structure but different values
- completely identical trees

Time complexity: O(n), because each node position is checked once.

Space complexity: O(h) for iterative DFS, where h is the tree height. In the worst case of a completely skewed tree, h can be O(n).
"""
