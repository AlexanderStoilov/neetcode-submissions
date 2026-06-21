class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort - genius stuff
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        ordered_lists = [[] for _ in range(len(nums) + 1)]
        for num in freq:
            ordered_lists[freq[num]].append(num)
        top_k_elements = []
        for i in range(len(ordered_lists)-1, -1, -1):
            if k == 0:
                break
            while len(ordered_lists[i]) >= 1: # there is an element
                top_k_elements.append(ordered_lists[i].pop())
                k -= 1
        return top_k_elements

    ## time: O(n) # outer loop is O(n), inner is O(k), we add them to O(n + k) == cos k<=n == O(n).
    # Why adding explanation: That's the trick with this shape of nested loop (it's a common pattern, not exclusive to bucket sort): the inner loop's total work isn't "per outer iteration," it's bounded globally by something else in your code.
    ## space: O(n) # ordered lists has n+1 slots and in them, n elements dispersed. So O(n+n) = O(n)
        
