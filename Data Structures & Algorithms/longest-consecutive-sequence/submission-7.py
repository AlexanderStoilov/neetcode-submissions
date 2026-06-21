class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # naive solution - sort
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        print(f"sorted = {nums}")
        cur_seq = 0
        max_seq = 0
        included = set()
        for i in range(len(nums)):
            if i-1 >= 0 and nums[i] == nums[i-1]:
                continue
            elif i-1 >= 0 and nums[i] == nums[i-1] + 1:
                cur_seq += 1
            else:
                cur_seq = 1
            max_seq = max(max_seq, cur_seq)
        return max_seq
            


        