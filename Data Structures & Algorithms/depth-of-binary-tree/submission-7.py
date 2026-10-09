# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
        if not root:
            return 0

        depth = 0
        level = [root]
        while level:
            next_level = []
            depth += 1

            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
    
            level = next_level # next_level reinitialized on next iteration, so no "2 pointers -> 1 list" problem
        
        return depth

"""
I decided to solve Maximum Depth of Binary Tree with BFS, processing the
tree one level at a time.

My first BFS version stored both nodes and their depths in a deque. It
also added both children without checking them first:

    level.append((node.left, depth + 1))
    level.append((node.right, depth + 1))

This worked because the loop checked whether each node was None before
using it. However, every leaf added two unnecessary None entries. The
algorithm was still O(N), but it did extra work and used more queue space.

I improved it by returning early for an empty tree and only adding real
children:

    if node.left:
        level.append((node.left, depth + 1))
    if node.right:
        level.append((node.right, depth + 1))

That deque version was correct. It stored a depth with every node, even
though all nodes currently in the same BFS level have the same depth.

I then tried to remove deque and use a normal list. My first attempt was:

    level = [[(root, 1)]]

    while level:
        node, depth = level.pop()
        ...
        level = next_level[::-1]

The extra brackets made level a list containing another list, so pop()
returned a list instead of a tuple. Unpacking it as node and depth was
wrong.

Even after fixing the brackets, replacing level after processing only
one node would discard the other nodes waiting in the same level. Also,
pop() from the end is LIFO behavior. That is useful for a stack, but by
itself it is not BFS. Reversing a list does not fix the fact that the
remaining siblings were discarded.

The next version processed every node in the current level first:

    level = [(root, 1)]

    while level:
        next_level = []

        for node, depth in level:
            if node.left:
                next_level.append((node.left, depth + 1))
            if node.right:
                next_level.append((node.right, depth + 1))

        level = next_level[::-1]

This was correct. Reversing the next level was unnecessary, though.
Node order inside a level does not affect the maximum depth. The slice
also creates a copy and costs O(K), where K is the size of that level.
Across the complete algorithm the total copying is still O(N), but there
is no reason to do it.

I then realized I did not need to store depth with every node. The outer
loop already represents one complete level, so I can increase depth once
per loop:

    depth = 0
    level = [root]

    while level:
        depth += 1
        next_level = []

        for node in level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        level = next_level

I first started depth at 1 and increased it before processing the level.
That caused an off-by-one error: a tree containing only the root returned
2. Starting at 0 fixes this because depth increases exactly once for each
non-empty level.

Assigning level = next_level is safe. Both names refer to the same list
for a moment, but next_level is rebound to a fresh list at the beginning
of the next loop. The old list is not being mutated after it becomes the
current level.

The empty-tree case returns 0. A tree with only the root returns 1. A
one-sided tree continues creating one next level at a time until its
depth equals its number of nodes.

Time Complexity: O(N), because every node is processed once.

Space Complexity: O(W), where W is the maximum width of the tree. The
current and next levels are stored, so the worst case is O(N).
"""

"""
Assume N means the number of real nodes in a non-empty binary tree.

The BFS version appends both child slots for every real node:

    queue.append(node.left)
    queue.append(node.right)

Therefore, it appends 2N child references in total.

A tree with N nodes has N - 1 real child links. The root has no parent,
and every other node has exactly one parent.

So the remaining child slots must be None:

    None slots = total child slots - real child links
               = 2N - (N - 1)
               = N + 1

For example:

    root
      \
      middle
          \
          leaf

Here N = 3.

There are 2N = 6 child slots:

    root:   [None, middle]
    middle: [None, leaf]
    leaf:   [None, None]

There are N - 1 = 2 real links and N + 1 = 4 None slots.

The N + 1 None values are processed over the whole run, but they are not
all necessarily in the queue at the same time. Space complexity measures
the peak queue size.

Let W be the maximum number of real nodes at one level. If a level has W
leaf nodes, the algorithm adds 2W None entries for the next level. The
queue is therefore up to a constant factor larger:

    O(2W) = O(W)

Since W can be N in the worst case, the worst-case space complexity is
O(N). Checking before appending does not change the Big-O complexity, but
it avoids the extra None entries and uses less memory in practice.
"""
