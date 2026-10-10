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
