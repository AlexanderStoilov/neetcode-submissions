class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for mid in range(1, len(nums)-1):
            left = 0
            right = len(nums)-1
            while left < mid < right:
                total = nums[left] + nums[mid] + nums[right]
                if total == 0:
                    triplet = [nums[left], nums[mid], nums[right]]
                    res.add(tuple(sorted(triplet))) # if no sorting, it fails on input [0,0,0,0,...]
                    # could have multiple triplets with same mid
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return list(res)
