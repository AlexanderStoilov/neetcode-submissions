class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        buckets = [ [] for _ in range(len(nums)+1) ]
        for num, cnt in freq.items():
            buckets[cnt].append(num)
        res = []
        for i in range(len(buckets)-1, -1, -1):
            if k == 0:
                break
            for num in buckets[i]:
                res.append(num)
                k -= 1
        return res
