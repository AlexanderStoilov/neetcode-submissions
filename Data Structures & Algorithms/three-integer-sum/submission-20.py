class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3. two pointers
        nums.sort()
        res  = []
        left = 0
        # for left in range(len(nums)):
        while left <= len(nums) - 1:
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                total = nums[left] + nums[mid] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    mid += 1
                else:
                    res.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                    right -= 1
                    while mid < right and nums[right] == nums[right + 1]:
                        right -= 1
            left += 1
            while left <= len(nums) - 1 and nums[left] == nums[left - 1]:
                left += 1
        return res