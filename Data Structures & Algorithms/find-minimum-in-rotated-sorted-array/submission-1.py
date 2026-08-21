class Solution:

    # log(n) solution
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if nums[left] < nums[right]:
            # array is in original state
            return nums[left]

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                # smallest element is on the right
                # case: (1 2 3 4 5 6)
                left = mid + 1
            elif mid - 1 >= 0 and nums[mid-1] > nums[mid]:
                # we need an additional case for when we land at the min element already, instead of going to the left
                # case: (5 6 [1] 2 3 4)
                return nums[mid]
            else:
                # smallest element is on the left
                 # case: (5 6 1 [2] 3 4)
                right = mid - 1

        return nums[left]
            



"""


1 2 3 4 5 6
5 6 1 2 3 4
3 4 5 6 1 2



"""