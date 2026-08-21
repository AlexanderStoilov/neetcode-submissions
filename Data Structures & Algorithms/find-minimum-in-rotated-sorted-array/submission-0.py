class Solution:
    def findMin(self, nums: List[int]) -> int:
        # trivial solution - O(n)
        smallest = float('inf')
        for num in nums:
            if num < smallest:
                smallest = num
        return smallest