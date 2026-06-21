class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref1 = nums.copy()
        pref2 = nums.copy()
        for i in range(1, len(pref1)):
            pref1[i] *= pref1[i-1]
        for i in range(len(pref2)-2, -1, -1):
            pref2[i] *= pref2[i+1]

        print(pref1)
        print(pref2)

        res = []
        for i in range(len(nums)):
            left = pref1[i-1] if i >= 1 else 1
            right = pref2[i+1] if i+1 <= len(nums) - 1 else 1
            total = left * right
            res.append(total)
        return res