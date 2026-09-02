class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if nums[left] <= nums[mid]: # we are in left partition / there are no partitions
                    left = mid + 1
                else: # we are in right partition
                    if target < nums[left]:
                        left = mid + 1
                    else: 
                        right = mid - 1
            elif target < nums[mid]:
                if nums[left] <= nums[mid]: # we are in left partition / there are no partitions
                    if target < nums[left]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else: # we are in right partition
                    right = mid - 1
           
        return -1

"""
4 (5) 6 1 2 3
4 5 6 1 (2) 3 


1 2 (3) 4 5 6
3 4 (5) 6 1 2 
5 6 (1) 2 3 4
5 6 1 (2) 3 4

"""