class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(numbers):
            if target - num in seen:
                return [seen[target-num], idx+1]
            else:
                seen[num] = idx+1