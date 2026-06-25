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
                    triple = [nums[left], nums[mid], nums[right]]
                    res.add(tuple(sorted(triple))) # if no sorting, it fails on input [0,0,0,0,...]
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return list(res)
