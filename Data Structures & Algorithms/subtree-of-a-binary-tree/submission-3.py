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
                isSubtree = areSameTree(cur, subRoot)
                if isSubtree:
                    return True

            tree1.append(cur.left)
            tree1.append(cur.right)

        return False # 'subroot' start not found in 'root'

        
        