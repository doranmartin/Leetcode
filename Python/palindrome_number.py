class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        end = len(x) - 1
        for index, digit in enumerate(x):
            if end == index:
                break
            elif x[index] != x[end]:
                return False
            end -= 1

        return True
