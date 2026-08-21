"""
Started with the brute force — linear scan, O(n), nothing interesting:

    smallest = float('inf')
    for num in nums:
        if num < smallest:
            smallest = num
    return smallest

Then went for the O(log n) binary search. First mistake: spent time mentally
solving "search for a target element in a rotated sorted array" — a different
problem entirely. Got tunnel vision thinking I already knew this one, and only
realized mid-way that finding the *minimum* is a different task. Refocused.

The core insight for binary search here: comparing nums[mid] to nums[right]
tells you unambiguously which half the minimum lives in. If nums[mid] > nums[right],
the right half is "out of order" (the rotation happened there), so the minimum
must be somewhere in [mid+1, right]. Otherwise, the right half is clean and sorted,
meaning the minimum is at 'mid' or somewhere in [left, mid-1], so essentially somewhere in [left, mid].

First working version used three explicit cases:

    if nums[left] < nums[right]:
        return nums[left]  # array unrotated, leftmost is smallest

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        elif mid - 1 >= 0 and nums[mid-1] > nums[mid]:
            return nums[mid]
        else:
            right = mid - 1

Two bugs hit during development here:

Bug 1 — missed the "already at minimum" case entirely on the first attempt.
When mid lands exactly on the minimum element (e.g. [5, 6, <1>, 2, 3, 4] with
mid=2 pointing at 1), the else branch would do right = mid - 1, stepping *past*
the minimum and losing it. Needed the explicit elif to catch it:

    elif mid - 1 >= 0 and nums[mid-1] > nums[mid]:
        return nums[mid]

Bug 2 — wrote the elif condition inverted: nums[mid-1] < nums[mid] instead of >.
Was thinking "when is this NOT the minimum?" and forgot to flip the sign. Classic.
The correct read: "the previous element is *larger* than mid, so mid is a local
drop — that's the inflection point, that's the minimum."

Also needed the mid - 1 >= 0 boundary guard because when mid = 0, mid - 1 = -1
which wraps to the last element in Python — a silent wrong answer, not a crash.

This three-case version passes, but it's more complex than necessary. The cleaner
insight: use right = mid instead of right = mid - 1 in the else branch. This keeps
mid inside the search space (since mid itself could be the answer), so the while
loop naturally converges to left == right pointing at the minimum — no explicit
"am I already there?" check needed, no early return for the unrotated case needed,
no boundary guard on mid - 1 needed. Three cases collapse to two:

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

Why compare to nums[right] and not nums[left]?
If you compared nums[mid] against nums[left]:

nums[mid] > nums[left] — mid is in the left sorted portion, but the minimum could still be anywhere to the right, OR left itself could be the minimum if the entire right portion is lower. You can't cleanly decide which half to eliminate.
nums[mid] < nums[left] — the minimum is somewhere in [left+1, mid], but you'd need to be careful not to exclude mid.

nums[right] always gives an unambiguous signal: if mid > right, the right half is
broken; if mid <= right, the right half is clean. No ambiguous case exists.

time: O(log n) — each iteration either moves left past mid or pulls right down to
                  mid, halving the search space every time. At most log2(n) iterations.
space: O(1) — only left, right, mid; no auxiliary structures.
"""

class Solution:
    
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                # smallest is on the right 
                    left = mid + 1
            else:
                # smallest is on the left, OR at mid
                    right = mid

        return nums[left]