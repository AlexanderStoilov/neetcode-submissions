class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        options = {}
        for idx, val in enumerate(nums):
            if val in options:
                options[val].append(idx)
            else:
                options[val] = [idx]

        for idx, val in enumerate(nums):
            if target - val in options:
                places = options[target-val]
                if idx != places[0]:
                    return [idx, places[0]]
                elif len(places) >= 2:
                    return [idx, places[1]]
