class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        heap = []
        for num, cnt in freq.items():
            heapq.heappush(heap, (-cnt, num)) # by default heapq is min heap
            # switching the '-' transforms it into a max heap (40, 50 -> -50, -40)
            # since we don't care about cnt value after, we don't have to reverse it with '-'
            # but usually that's how it works
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        # n = len(nums)
        ## time: O(n.logn) | O(k.logn) for the heap popping, O(n.logn) for heap pushing
        ## space: O(n)
