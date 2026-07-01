class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ## two pointers
        # water amount = (distance between bars) * (min of the 2 heights)
        # we move from the shorter bar inwards
        # on each step we potentially update max_water
        # time: O(n)
        # space: O(1)
        left = 0
        right = len(heights) - 1
        max_water = 0
        while left < right:
            cur_water = (right - left) * min(heights[left], heights[right]) # distance does NOT need "right-left+1" cos the space is BETWEEN them only (easiest - visualize on example map)
            max_water = max(max_water, cur_water)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_water


"""
Why prefix sums don't work for Container With Most Water
---------------------------------------------------------

Prefix sums work when a quantity is "separable" — meaning you can express it as
g(j) - g(i) for some precomputed function g. The sum of a subarray [i,j] is the
classic example: prefix[j] - prefix[i-1] gives you the answer in O(1) after O(n)
precomputation. The reason this works is that summation is additive — elements
contribute independently to the total, so you can factor out the left boundary
as a simple subtraction.

The water container formula is: (right - left) * min(heights[left], heights[right])

This fails the separability requirement in two independent ways.


PROBLEM 1: min(heights[left], heights[right]) is not separable
--------------------------------------------------------------
For prefix decomposition to work, we'd need some function g such that:
    g(j) - g(i) = min(heights[i], heights[j])    for ALL pairs (i, j)

Let's try to construct such a g on a concrete example and see what happens.

heights = [3, 1, 4]

The three pairs give us:
    min(heights[0], heights[1]) = min(3, 1) = 1  →  g(1) - g(0) = 1
    min(heights[0], heights[2]) = min(3, 4) = 3  →  g(2) - g(0) = 3
    min(heights[1], heights[2]) = min(1, 4) = 1  →  g(2) - g(1) = 1

But from the first two equations:
    g(2) - g(1) = (g(2) - g(0)) - (g(1) - g(0)) = 3 - 1 = 2

The third equation says g(2) - g(1) = 1. Contradiction. 2 ≠ 1.

No such function g exists, even for a three-element array. You can attempt this
construction on any heights array and you'll hit the same wall. The reason is
fundamental: min(a, b) is a *comparison* — it selects one of its two arguments
based on their relative magnitudes. That selection creates a dependency between
both endpoints that can't be precomputed independently at each index. The value
min(heights[i], heights[j]) is not a property of j alone minus a property of i
alone — it's a property of the *relationship* between heights[i] and heights[j],
specifically which one is smaller. No matter what you precompute at each index
in isolation, you can't capture a relational property without examining both
endpoints together at query time.


PROBLEM 2: even if both components WERE separable, their product wouldn't be
-----------------------------------------------------------------------------
Suppose hypothetically you had two separable quantities:
    f(i, j) = g(j) - g(i)      for some precomputed g
    h(i, j) = p(j) - p(i)      for some precomputed p

Their product expands via FOIL:
    f(i,j) * h(i,j) = (g(j) - g(i)) * (p(j) - p(i))
                     = g(j)·p(j)  -  g(j)·p(i)  -  g(i)·p(j)  +  g(i)·p(i)

For this to be expressible as q(j) - q(i) for some precomputed q, you'd need
a function of j alone minus a function of i alone. But the cross terms g(j)·p(i)
and g(i)·p(j) each simultaneously depend on both endpoints and cannot be absorbed
into either "a function of j only" or "a function of i only". They are inherently
about the interaction between both indices.

This is a general algebraic fact: separability is closed under addition but NOT
under multiplication. The sum of two separable quantities is separable:
    (g(j) - g(i)) + (p(j) - p(i)) = (g(j) + p(j)) - (g(i) + p(i)) = q(j) - q(i)
    where q(x) = g(x) + p(x)   ✓

But the product introduces cross terms that destroy the structure entirely. So
even in a hypothetical world where min() was somehow separable, the fact that the
water formula multiplies distance by height would independently break any attempt
at prefix decomposition.


CONCLUSION
----------
The water container formula (right - left) * min(heights[left], heights[right])
is not separable for two compounding reasons: min() is a relational comparison
that fundamentally cannot be precomputed independently at each index, and even
if it could, the product structure introduces cross terms that kill separability.
Prefix sums require algebraic decomposability that simply isn't present here.

The two-pointer approach works for a completely different mathematical reason —
not algebraic decomposition, but a *dominance argument*: when left is the shorter
bar, no pair (left, right') for any right' < right can beat the current water,
because distance strictly shrinks while the height cap stays bounded by
heights[left]. This lets you provably discard entire classes of pairs in O(1),
achieving O(n) total without any precomputation.
"""


"""
Why Kadane's algorithm doesn't apply to Container With Most Water
-----------------------------------------------------------------

Kadane's algorithm solves the maximum subarray problem in O(n) time by maintaining
a single running value — the best subarray sum ending at the current index — and
making a local binary decision at each step: either extend the existing subarray
to include the current element, or start a fresh subarray at the current element.
The decision rule is clean: if the running sum is positive, extending it can only
help; if it's negative, it's a liability and you're better off starting fresh.
This works because subarray sums are additive — each element contributes its full
value independently, and a negative running sum is always strictly worse than
abandoning it.

For Kadane's to apply to a problem, that problem needs to satisfy a very specific
set of structural requirements. Container With Most Water fails all of them.


REQUIREMENT 1: the value must be computable from a single running scalar
------------------------------------------------------------------------
Kadane's state at any point in the algorithm is exactly one number: the best sum
ending at the current position. This is sufficient for max subarray because the
contribution of any element nums[i] to a subarray ending at i is just nums[i]
itself — fixed, independent of which other elements are in the subarray. You don't
need to remember anything about the subarray's history beyond its running total.

The water container value is: (right - left) * min(heights[left], heights[right])

This depends on TWO indices simultaneously — both the left bar and the right bar —
and their distance from each other. There is no single scalar "running water value
ending at index i" that you can maintain, because the value of any pair is not a
property of one endpoint with some accumulated history — it's a function of the
specific combination of both endpoints together. You can't reduce this to a single
running state without losing essential information about where the other endpoint is.


REQUIREMENT 2: there must be a clean local binary decision at each step
-----------------------------------------------------------------------
Kadane's power comes from the fact that at each index i, you only need to answer
one question with a binary answer: is the running sum positive (extend) or negative
(restart)? This decision is complete — you don't need to look ahead, and you don't
need to consider any other historical context. The current running sum encodes
everything relevant about the past.

In the water container problem, there is no analogous local decision you can make
by examining a single bar in isolation. A very short bar might be part of the
optimal pair if it happens to be positioned very far from a very tall bar. A very
tall bar might be irrelevant if its nearest neighbors are all tiny. Whether any
given bar is "worth keeping" as part of the optimal solution depends entirely on
global positional context — specifically, what other bars exist at what distances.
There is no local signal at index i that tells you "this bar is definitely part
of the optimal solution" or "this bar is definitely not." The binary decision that
Kadane's requires simply doesn't exist here.


REQUIREMENT 3: optimal substructure must take the form "best ending at i depends
only on best ending at i-1 plus current element"
---------------------------------------------------------------------------
Kadane's is a specific instance of dynamic programming where the recurrence is:

    best_ending_at[i] = max(nums[i], best_ending_at[i-1] + nums[i])

This recurrence works because the optimal subarray ending at i either starts fresh
at i, or extends the optimal subarray ending at i-1. The key word is "ending at
i-1" — the transition only looks one step back, and it only depends on a single
accumulated value. This is an extremely tight and clean recurrence structure.

The water container problem has no recurrence of this form. The optimal pair
(left, right) has no meaningful relationship to the optimal pair involving
right-1 or left+1. You can't say "the best container with right boundary at j
can be computed from the best container with right boundary at j-1 plus some
current contribution," because the value function isn't additive across steps —
it's a product of distance and minimum height, both of which change
non-incrementally as you move either boundary.


REQUIREMENT 4: the "bottleneck" structure of min() is incompatible with Kadane's
---------------------------------------------------------------------------------
In max subarray, every element contributes its full value to the sum. A positive
element always helps, a negative element always hurts, and the magnitude of that
help or hurt is exactly the element's value — no more, no less. This linearity
is what makes the extend-vs-restart decision clean and complete.

The min() function in the water formula introduces a bottleneck: the shorter of
the two bars caps the entire container's height, regardless of how tall the other
bar is. This means a very tall bar can be made completely irrelevant by a short
neighbor — its height contributes nothing beyond what the short bar already
provides. This kind of winner-takes-none bottleneck structure is the opposite of
the additive independence that Kadane's requires. You can't reason about a bar's
"contribution" in isolation because its effective contribution is always contingent
on what it's paired with — specifically whether it's the taller or shorter bar in
the pair.


WHAT KADANE'S AND TWO POINTERS ACTUALLY HAVE IN COMMON (and where they differ)
-------------------------------------------------------------------------------
It's worth understanding why Kadane's feels like it should generalize here —
both algorithms scan an array in O(n) and maintain some kind of running best
value. The superficial similarity is real. But the mathematical engines underneath
are completely different:

Kadane's works via a LOCAL recurrence — the optimal solution at each position
is a direct function of the optimal solution at the previous position plus the
current element. It's dynamic programming with a one-step lookback and additive
transitions.

Two pointers works via a DOMINANCE ARGUMENT — at each step, you prove that an
entire class of candidate pairs is provably suboptimal and can be discarded. When
left is the shorter bar, no pair (left, right') for any right' < right can beat
the current water, because distance strictly shrinks while the height cap stays
bounded by heights[left]. This isn't a recurrence — it's a proof that certain
candidates are dominated and can be skipped entirely. The algorithm's efficiency
comes from collapsing an O(n²) search space by repeatedly proving large chunks
of it are irrelevant.

These are fundamentally different mathematical principles — local recurrence vs
global dominance — and Container With Most Water belongs firmly in the dominance
camp. Kadane's local recurrence machinery has nothing to grab onto here.
"""