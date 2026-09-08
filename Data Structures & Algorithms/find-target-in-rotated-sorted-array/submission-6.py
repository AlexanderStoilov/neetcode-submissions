"""
Spent multiple days on search-in-rotated-sorted-array. The array is
ascending and then rotated once, so it is two sorted runs stuck together
(or one run if it never rotated):

    [4, 5, 6, 1, 2, 3]          [0, 1, 2]
     ^^^^^^^  ^^^^^^^            ^^^^^^^
     left/big  right/small       no drop

I wanted one binary search, so the loop was the usual one from the start:

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        ...
    return -1

Vanilla "mid too small → right, mid too big → left" dies here because
smaller than mid does not mean left of mid. Target can sit on the other
side of the drop. So I classified mid with nums[left] <= nums[mid]
("[left, mid] is sorted / we are in the left run, or there is no drop")
and nested the mid-vs-target compare on top of that. First version that
passed every test:

    class Solution:
        def search(self, nums: List[int], target: int) -> int:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    if nums[left] <= nums[mid]:
                        left = mid + 1
                    else:
                        if target < nums[left]:
                            left = mid + 1
                        else:
                            right = mid - 1
                elif target < nums[mid]:
                    if nums[left] <= nums[mid]:
                        if target < nums[left]:
                            left = mid + 1
                        else:
                            right = mid - 1
                    else:
                        right = mid - 1
            return -1

Six exits. Two of them needed a wrap check, and I had the wrong one
for a long time. In the target < mid / left-run branch I wrote:

    if target <= nums[right]:
        left = mid + 1
    else:
        right = mid - 1

instead of:

    if target < nums[left]:
        left = mid + 1
    else:
        right = mid - 1

target <= nums[right] was me asking "does target fit on the right end?"
That only makes sense while the window is still rotated, because then
nums[right] is the max of the small run. Binary search constantly
produces unrotated windows. In those, nums[right] is just the max of
the whole window, so the check is true for every plausible target and
we only ever walk right. Caught it on [0, 1, 2], target = 0:

    left, right = 0, 2
    mid = 1, nums[mid] = 1
    0 < 1, [0, 1] is sorted
    0 <= nums[2] (2) → left = 2
    mid = 2, nums[mid] = 2
    0 <= nums[2] (2) → left = 3
    return -1

nums[left] is the real fence: it is the minimum of the sorted left
half. If target is below that, it cannot live in [left, mid], rotated
or not. With target < nums[left] the same case goes right = 0 and
hits index 0.

That passing tree was already O(log n) / O(1). The rewrite was just
asking the same questions in the order the array actually gives you.
Flip the nesting so "is [left, mid] sorted?" is on the outside, then
collapse each side. On the left-sorted side we go left in exactly one
case — nums[left] <= target < nums[mid] — and right otherwise. That
interval is the wrap check we already had, written as a range. On the
right-sorted side we go right in exactly one case. I had that as
nums[mid] < target < nums[left]. In this branch the window is rotated,
so [mid, right] is sorted and every right-run value is < nums[left],
and for a target that exists that cut is the same as
nums[mid] < target <= nums[right]. That swap is legal only here.
nums[right] is actually the top of the half we are testing. It was
not a stable fence in the other branch, which is why the old
target <= nums[right] blew up.

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

Same three indices, four leaves instead of six. After the equality
check the only question is: which half around mid is a normal sorted
interval, and is target inside it? If yes stay, if no throw that
half away. [0, 1, 2], target = 0 is just "left half is [0, 1], 0 is
in it" — no wrap story. The comment I kept writing as
"we are in the left/right part" is really "this half is sorted."

Time:  O(log n) — each step discards a half, same as vanilla binary
       search. The rewrite does not make it faster than the first
       passing tree; it just holds the invariant in one range check.
Space: O(1) — left, right, mid. No extra arrays, no recursion.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: # we are in left part
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # we are in right part
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
 
