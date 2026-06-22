class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {} # not needed; upper bound estimate, otherwise would be expensive to track all branches

    def add(self, val):
        self.parent[val] = val
        self.rank[val] = 1

    def get_root(self, val):
        if val == self.parent[val]:
            return val
        self.parent[val] = self.get_root(self.parent[val])
        return self.parent[val]

    def union(self, val1, val2):
        root1 = self.get_root(val1)
        root2 = self.get_root(val2)
        if root1 == root2: # Already unionized
            return

        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = self.parent[root2]
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = self.parent[root1]
        else: # equal ranks => when adding one subtree onto the other, the rank of the recipient one will increase by 1
            self.parent[root1] = self.parent[root2]
            self.rank[root2] += 1
        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set()
        for num in nums:
            numset.add(num)
       
        uf = UnionFind()
        for num in nums:
            uf.add(num)
        for num in nums:
            if num-1 in numset:
                uf.union(num, num-1)
            if num+1 in numset:
                uf.union(num, num+1)
        
        # Now the question is, since in 'uf' we now have all roots settled (num-1,num,num+1),
        # which root is seen the most? That root corresponds to the biggest chain

        root_freq = {}
        for num in numset: # Important, if we have diplucates we should ignore them
            cur_root = uf.get_root(num)
            root_freq[cur_root] = root_freq.get(cur_root, 0) + 1

        print(root_freq)

        max_root_freq = 0
        for root, freq in root_freq.items():
            if freq > max_root_freq:
                max_root_freq = freq
        
        return max_root_freq



        

        
        

        