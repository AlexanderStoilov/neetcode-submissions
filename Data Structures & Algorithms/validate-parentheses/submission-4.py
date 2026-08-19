"""
Valid Parentheses — Two Approaches
-----------------------------------

APPROACH 1: helper method closesTop()
Stack-based. Push every character onto the stack. Before pushing, check if the
current character closes the top of the stack — if it does, pop instead of push.
At the end, a valid string has an empty stack (every opener was matched and closed).

Edge case: a closing bracket with an empty stack (e.g. "]abc") must not pop —
closesTop() guards this with an early 'not brackets' check.

APPROACH 2: opening→closing dictionary
Same stack logic, but replaces the helper with a dict mapping each opener to its
expected closer: {'(': ')', '{': '}', '[': ']'}.

The condition 'stack[-1] in pairs and pairs[stack[-1]] == cur' checks:
  1. the top of the stack is an opening bracket (it's a key in pairs)
  2. the current character is exactly its expected closer

Closing brackets that land on the stack (invalid input) are never keys in pairs,
so they can never be matched or popped — they sit permanently and cause the final
'not stack' check to correctly return False.

time: O(n) — single pass through s
space: O(n) — stack holds at most n characters (worst case: all opening brackets)

APPROACH 3: closing→opening dictionary (conventional pattern)
--------------------------------------------------------------
The most common pattern seen in solutions and interviews. Inverts the dictionary
to map each closer to its expected opener:
    pairs = {')': '(', '}': '{', ']': '['}

The loop first checks if cur is a closing bracket (cur in pairs). If it is, check
if the top of the stack is the expected opener (stack[-1] == pairs[cur]). If not,
the string is invalid — return False immediately rather than continuing. Otherwise,
pop. If cur is an opening bracket, push it.

    for cur in s:
        if cur in pairs:
            if not stack or stack[-1] != pairs[cur]:
                return False
            stack.pop()
        else:
            stack.append(cur)

The advantage of this direction: checking 'cur in pairs' to detect closing brackets
reads more naturally left-to-right ("is what I'm currently looking at a closer?"),
and the early return False on mismatch avoids pushing invalid characters onto the
stack entirely — so the stack only ever contains opening brackets, never closing ones.
This makes the stack's contents semantically cleaner: it's purely a record of
unmatched openers waiting to be closed.

All three approaches are correct and have identical complexity.

time: O(n) — single pass through s
space: O(n) — stack holds at most n characters in the worst case (all opening brackets,
              e.g. s = "((((((")
"""

class Solution:
    def closesTop(self, brackets: list, cur: chr):
        if not brackets:
            return False

        top_el = brackets[-1]
        if ((top_el == '(' and cur == ')') or
            (top_el == '{' and cur == '}') or
            (top_el == '[' and cur == ']')):
                return True
        return False

    def isValid(self, s: str) -> bool:
        brackets = []
        for c in s:
            if self.closesTop(brackets, c):
                brackets.pop() # by def - last el (-1), compl = O(1)
            else:
                brackets.append(c)
        
        return len(brackets) == 0

