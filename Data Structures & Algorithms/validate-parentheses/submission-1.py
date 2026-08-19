class Solution:
    def closesTop(self, brackets: list, cur: chr):
        if not brackets or len(brackets) == 0:
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

