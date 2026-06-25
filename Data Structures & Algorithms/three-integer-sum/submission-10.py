class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()  # if no uniqueness, it fails on input [0,0,0,0,...]
        for mid in range(1, len(nums)-1):
            left = 0
            right = len(nums)-1
            while left < mid < right:
                total = nums[left] + nums[mid] + nums[right]
                if total == 0:
                    triplet = [nums[left], nums[mid], nums[right]]
                    res.add(tuple(triplet)) # sorting unnecessary, left-mid-right always sorted due to input sorting
                    # could have multiple triplets with same mid
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return list(res)

        # time: O(n^2) | n.logn for initial sorting, n for iteration for mid, and n total moves for left & right for each mid. Sorting the triplet is O(1) cos always 3 elements
        # space: O(n)
