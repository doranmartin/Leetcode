class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for char in s:
            if char in map:
                stack.append(map[char])
            elif len(stack) == 0 or char != stack.pop():
                return False
        
        return len(stack) == 0
