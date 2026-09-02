"""
We've been grinding search-in-rotated-sorted-array for days. The array is
ascending, then rotated once, so it looks like two sorted runs glued together:

    [4, 5, 6, 1, 2, 3]
     ^^^^^^^  ^^^^^^^
     left/big  right/small

or sometimes there's no rotation at all:

    [0, 1, 2]

We wanted one binary search, not a linear scan, so the skeleton was the usual
"safe mid" loop we already trust:

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        ...
    return -1

The fight was everything after the equality check. Normal binary search says
"mid too small → go right, mid too big → go left". That dies here because
"smaller than mid" does not mean "left of mid". Target can sit on the other
side of the drop.

So we classified mid first:

    nums[left] <= nums[mid]  →  [left, mid] is sorted
                                (mid is in the left/big run, or the window
                                 isn't rotated at all)
    else                     →  the drop is inside [left, mid]
                                (mid is in the right/small run)

and then nested the usual mid-vs-target comparison on top of that. That's how
we ended up with a 3-level if tree instead of one range check.

The version that finally passed:

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

Walk of the four situations, because this is where we kept lying to ourselves.

1) mid < target, and [left, mid] is sorted.
   Everything from left..mid is <= nums[mid] < target, so target cannot be in
   this half. Always cut left:

        left = mid + 1

   No third-level if. This one we actually got right early.

2) mid < target, and mid is in the right/small run.
   Target is bigger than a small number. It might still be a small number to
   the right of mid, or it might be one of the big numbers on the left side
   of the drop. The left run starts at nums[left], and every small value is
   < nums[left], so:

        if target < nums[left]:
            left = mid + 1    # still in the small run, go right
        else:
            right = mid - 1   # target belongs with the big run, jump left

3) target < mid, and [left, mid] is sorted. THIS is the branch that ate us.
   Target is smaller than a value in the big run. Two homes:
   - it's still in the big run, between nums[left] and mid → go left
   - it's too small to live in the big run, so it wrapped into the small
     run on the right → go right

   The correct cut is "can target even exist in [left, mid)?":

        if target < nums[left]:
            left = mid + 1
        else:
            right = mid - 1

4) target < mid, and mid is in the right/small run.
   Mid is already a small number, target is smaller than that, and every
   left-run value is bigger than every right-run value. Target cannot be
   on the left. Always:

        right = mid - 1

We spent a long time with the wrong third-level test in branch 3:

        if target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1

The idea was "if target fits on the right end, walk right". That is a
rotation-only thought. When the array (or the current window) is rotated,
nums[right] is the max of the small run, so the check accidentally works
on a bunch of rotated examples:

    4 (5) 6 1 2 3     target in {1,2,3}  →  target <= 3, go right  (lucky)
    3 4 (5) 6 1 2     target = 4          →  4 <= 2 is false, go left (lucky)

Then the window shrinks. Binary search constantly produces unrotated
subarrays even if the original input was rotated. In an unrotated window
nums[right] is the max of the whole window, so target <= nums[right] is
true for every plausible target and we only ever walk right.

That's exactly [0, 1, 2], target = 0:

        nums = [0, 1, 2], target = 0
        left, right = 0, 2
        mid = 1, nums[mid] = 1
        0 < 1, [0, 1] is sorted
        buggy:  0 <= nums[2] (2) → left = 2
        mid = 2, nums[mid] = 2
        0 < 2, [2, 2] is sorted
        buggy:  0 <= nums[2] (2) → left = 3
        return -1

        fixed:  0 < nums[left] (0) is false → right = 0
        mid = 0, nums[mid] = 0 → return 0

Same bug shows up on originally rotated inputs once the window becomes
sorted, e.g. [3, 4, 5, 6, 0, 1, 2] looking for 0 or 3. We thought we were
debugging "rotated array logic". We were actually debugging "what is
nums[right] after the window changes".

nums[left] is the right fence because it is the minimum of the sorted
left half. If target is below that, it cannot live in [left, mid],
rotated or not. nums[right] is not a stable fence: sometimes it's the
max of the small run, sometimes it's just "the current last element".

Scratch cases we kept redrawing while flipping those branches:

    4 (5) 6 1 2 3
    4 5 6 1 (2) 3
    1 2 (3) 4 5 6     # no rotation — the case that finally exposed us
    3 4 (5) 6 1 2
    5 6 (1) 2 3 4
    5 6 1 (2) 3 4

Final result: this code is correct. Every step throws away half the
window, so it is already asymptotically optimal. It is just a painful
way to hold the invariant — six leaf decisions, and two of them need a
wrap check that is easy to write against the wrong end of the array.

Time:  O(log n) — while left <= right, mid splits the window, one side
       is discarded each iteration, same as vanilla binary search.
Space: O(1) — a handful of indices. No extra arrays, no recursion.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if nums[left] <= nums[mid]: # we are in left partition / there are no partitions
                    left = mid + 1
                else: # we are in right partition
                    if target < nums[left]:
                        left = mid + 1
                    else: 
                        right = mid - 1
            elif target < nums[mid]:
                if nums[left] <= nums[mid]: # we are in left partition / there are no partitions
                    if target < nums[left]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else: # we are in right partition
                    right = mid - 1
           
        return -1

"""
4 (5) 6 1 2 3
4 5 6 1 (2) 3 


1 2 (3) 4 5 6
3 4 (5) 6 1 2 
5 6 (1) 2 3 4
5 6 1 (2) 3 4

"""