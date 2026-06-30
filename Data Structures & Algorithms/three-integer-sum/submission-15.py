class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j >= i + 2 and nums[j] == nums[j - 1]:
                    continue
                target = -nums[i] - nums[j]
                if target in count and count[target] >= 1:
                    res.append([nums[i], nums[j], target])
                
            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1

        return res

    # time: O(n^2)
    # space: O(n)
    # without the hashset to remove duplicates, cos we take care of it
