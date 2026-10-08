# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        # BFS, iteratively (cos recursively its a nigthmare :D)
        # Using deque cos its popleft O(1) and append (right side) O(1).
        # Python achieved this by using doubly linked list as the underlying structure.
        from collections import deque
        nodes = deque()
        nodes.append(root)
        while nodes:
            cur = nodes.popleft()
    
            cur.left, cur.right = cur.right, cur.left        
            if cur.left:
                nodes.append(cur.left)
            if cur.right:
                nodes.append(cur.right)
            
        return root
        
"""
I first solved Invert Binary Tree recursively. The helper visits the left
subtree, visits the right subtree, and then swaps the current node's two
child links.

I thought I needed to return every subtree:

    node.left = divide(node.left)
    node.right = divide(node.right)
    return node

That would not work with my helper because divide returns None. Assigning
that result back would remove the child. The tree is changed in place:
the parent already points to the same child object, and flip changes that
object directly. The original root object also stays the root, so I
return root.

I then wrote the same idea iteratively with DFS. The list is used as a
stack, so pop() removes the last item in O(1). Each node is swapped once
and its children are added to the stack. Checking whether a node has
children before swapping is correct, but optional. Swapping None with None
for a leaf is harmless.

I also wrote a BFS version with deque. popleft() and append() are both
O(1). In my first version, I added the children to the queue before
swapping the current node. That still works because the queue stores
references to the same child objects. Swapping the parent links does not
change those objects. Swapping first is a little clearer:

    cur.left, cur.right = cur.right, cur.left
    if cur.left:
        nodes.append(cur.left)
    if cur.right:
        nodes.append(cur.right)

The empty-tree case is handled by returning None. A leaf is also safe:
its two None links can be swapped without changing anything. A node with
only one child is handled correctly because the child moves to the other
side.

All versions take O(N) time because every node is processed once.

The recursive solution and iterative DFS use O(H) extra space, where H is
the tree height. That is O(log N) for a balanced tree and O(N) for a
one-sided tree.

The BFS solution uses O(W) extra space, where W is the maximum width of
the tree. Its worst case is O(N).
"""
        