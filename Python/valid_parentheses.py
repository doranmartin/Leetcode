class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for i in range(0, len(s) - 1, 2):
            if map[s[i]] == s[i + 1]:
                continue
            else:
                return False
            
        return True
    