class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums.copy()
        suffix = nums.copy()
        prefix[0] = 1
        suffix[-1] = 1

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-1, 0, -1):
            suffix[i-1] = suffix[i] * nums[i]
        
        print(f'prefix={prefix}')
        print(f'suffix={suffix}')

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        return res

        # n = len(nums)
        ## time: O(n)
        ## space: O(n)
    
        """
            1   2   4   6
                |
            1 x 4 x 6

og           1   2  4   6  

prefix      (1)  1  2   8
suffix      48  24  6  (1)

(x) - kept from the original arr. Cos we only begin the calc from second element
        """