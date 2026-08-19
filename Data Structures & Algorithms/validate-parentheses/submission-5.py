class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for cur in s:
            if stack and stack[-1] in pairs and pairs[stack[-1]] == cur: # if top el in stack is opening bracket, and cur closes it
                    stack.pop()
            else:
                stack.append(cur)
        return not stack