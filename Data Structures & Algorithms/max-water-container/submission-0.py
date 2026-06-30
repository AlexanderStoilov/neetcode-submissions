class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ## two pointers
        # water amount = (distance between bars) * (min of the 2 heights)
        # we move from the shorter bar inwards
        # on each step we potentially update max_water
        # time: O(n)
        # space: O(1)
        left = 0
        right = len(heights) - 1
        max_water = 0
        while left < right:
            cur_water = (right - left) * min(heights[left], heights[right]) # distance does NOT need "right-left+1" cos the space is BETWEEN them only (easiest - visualize on example map)
            max_water = max(max_water, cur_water)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_water