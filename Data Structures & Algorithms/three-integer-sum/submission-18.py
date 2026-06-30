class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 2. hashmap, alternative
        # alternative, if i wrongfully made the count decrease AFTER duplicate check (wrong)
        # then i would need to have the target >= nums[i]
        nums.sort()
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        res = []
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            count[nums[i]] -= 1
            for j in range(i + 1, len(nums)):
                if j >= i + 2 and nums[j] == nums[j - 1]:
                    continue
                count[nums[j]] -= 1
                target = -nums[i] - nums[j]
                if target in count and count[target] >= 1 and target >= nums[j]:
                    res.append([nums[i], nums[j], target])
                
            for j in range(i + 1, len(nums)):
                if j >= i + 2 and nums[j] == nums[j - 1]:
                    continue
                count[nums[j]] += 1

        return res

    # time: O(n^2)
    # space: O(n)
