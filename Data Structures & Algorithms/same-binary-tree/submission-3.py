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
