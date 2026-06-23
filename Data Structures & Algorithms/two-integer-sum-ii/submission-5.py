class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # binary search, embedded in a linear numbers traversal

        for i in range(len(numbers) - 1):
            search_val = target - numbers[i]

            # binary search for find search_val
            l = i + 1
            r = len(numbers) - 1
            while 0 <= l <= r <= len(numbers) - 1:
                mid = l + (r - l) // 2 ## safer way than  "(l + r) // 2" in strongly typed languages (not Python)
                if numbers[mid] == search_val:
                    return [i+1, mid+1]
                elif numbers[mid] < search_val:
                    l = mid + 1
                else:
                    r = mid - 1