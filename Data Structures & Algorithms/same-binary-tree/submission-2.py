# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS iterative

        if not p and not q:
            return True

        pStack = [p]
        qStack = [q]

        while pStack and qStack:
            pCur = pStack.pop()
            qCur = qStack.pop()

            # if (not pCur and not qCur):
                # continue

            if (pCur and not qCur) or (qCur and not pCur) or (pCur.val != qCur.val):
                return False

            # ---
            # draft on how we would have had to handle the Non check if we skip the check above 
            if (pCur.left and qCur.left):
                pStack.append(pCur.left)
                qStack.append(qCur.left)
            elif (pCur.left and not qCur.left) or (not pCur.left and qCur.left):
                return False
            
            if (pCur.right and qCur.right):
                pStack.append(pCur.right)
                qStack.append(qCur.right)
            elif (pCur.right and not pCur.right) or (not pCur.right and qCur.right):
                return False

            # ---

        if (pStack and not qStack) or (qStack and not pStack):
            return False

        return True
