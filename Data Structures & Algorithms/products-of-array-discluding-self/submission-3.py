class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zeros = 0
        for num in nums:
            if num == 0:
                count_zeros += 1
        
        res = []
        if count_zeros >= 2:
            for _ in nums:
                res.append(0)
        else:
            prod_nonzero = 1
            for num in nums:
                if num != 0:
                    prod_nonzero *= num

            for i in range(len(nums)):
                if nums[i] != 0:
                    if count_zeros == 1:
                        res.append(0)
                    else: # count_zeros == 0
                        res.append(prod_nonzero // nums[i])
                else: # nums[i] == 0
                    res.append(prod_nonzero)
        return res


    """
    1   2   3   0   4   | nonzero prod: 24
->  0   0   0   24  0

    1   2   3   5   4   | nonzero prod: 120
->  120 60  40  24  30

    1   2   0   0   4   | nonzero prod: 8
->  0   0   0   0   0


    time: O(n)
    space: O(1) auxiliary (excluding output), O(n) including it

    """