class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Absolute brute force would be iterate 3 loops -> O(n^3)
        # This is also O(n^3), but significantly uglier :)

        num_pos = defaultdict(set)
        for i in range(len(nums)):
            num_pos[nums[i]].add(i)

        res = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): # (i+1) technically not needed #1, the set tuple sorting and check will cover it, but this optimizes it further in the beginning - it doesn't process unnecessary duplications
                if i == j:
                    continue
                target = -nums[i]-nums[j]
                if target in num_pos:
                    set_cpy = num_pos[target].copy()
                    # Remove i and j from the set, and if there are any left indices,
                    #   for each one, where i<j<target_idx (to eliminate duplications), add to set
                    if i in set_cpy:
                        set_cpy.remove(i)
                    if j in set_cpy:
                        set_cpy.remove(j)
                    for target_idx in set_cpy: # 
                        if j < target_idx: # technically not needed #2, the set tuple sorting and check will cover it, but this optimizes it further in the beginning - it doesn't process unnecessary duplications  
                            # Using tuple for set value - immutable
                            # Sorting it, but since it always has 3 elements -> O(1)
                            # Then checking if that sorted tuple is present in the res set, if not
                            #   add it there
                            # SUPER ugly solution 
                            to_add = tuple(sorted([nums[i], nums[j], nums[target_idx]]))
                            if to_add not in res:
                                res.add(to_add)
        return list(res)


