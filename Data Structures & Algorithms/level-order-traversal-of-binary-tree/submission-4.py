# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            level_len = len(queue)
            cur_level_vals = []
            for _ in range(level_len):
                node = queue.popleft()
                cur_level_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(cur_level_vals)

        return result

"""
Started with BFS by levels using `level = [root]` and a separate `next_level`.
That solution was already correct, but it initially used two passes per level:
one to collect values and another to collect children. I streamlined it into one
loop that does both.

The key invariant is that, at the start of each outer iteration, `level`
contains exactly all nodes at one tree depth. `next_level` keeps children
separate, so different depths never get mixed.

I also considered a deque. My first deque attempt became messy because I
didn't yet know how to detect the end of a level. The key idea is to snapshot
`level_len = len(queue)` and process exactly that many nodes. Children appended
during those iterations remain in the queue for the next level.

Both the two-list frontier solution and the deque solution are valid. The final
deque version uses `popleft()`, which is efficient, and enqueues left children
before right children to preserve ordering.

Edge cases include an empty tree returning `[]`, a single-node tree, skewed
trees, and preserving left-to-right order.

Time Complexity: O(n), because every node is processed once.

Space Complexity: O(w) auxiliary space, where `w` is the maximum width of the
tree. The returned result itself uses O(n) space.
"""
        