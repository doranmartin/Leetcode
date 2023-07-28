class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = False
        a, b = list(a), list(b)
        big, small = max(a, b), min(a, b)
        i, j = len(big) - 1, len(small) - 1

        while j >= 0:
            if carry:
                if big[i] == '1' and small[j] == '1':
                    big[i] = '0'
                elif big[i] == '0' and small[j] == '0':
                    big[i] = '1'
                    carry = False
                else:
                    big[i] = '0'
            else:
                if big[i] == '1' and small[j] == '1':
                    big[i] = '0'
                    carry = True
                elif big[i] == '0' and small[j] == '0':
                    big[i] = '0'
                else:
                    big[i] = '1'

            i, j = i - 1, j - 1

        while i >= 0:
            if not carry:
                return str(big)
            else:
                if big[i] == '0':
                    big[i] == '1'
                    carry = False
            i -= 1

        if i < 0:
            new = '1'
            for char in big:
                new += char
            return str(new)

'''
keep track of carry boolean and index
figure out which is 'smaller' (less digits)
iterate backwards over small one, adding each digit
case 1 -> carry is true:
    if 1 + 1 -> 1, carry stays true
    if 1 + 0 -> 0, carry stays true
    if 0 + 0 -> 1, carry goes false
case 2 -> carry is false:
    1 + 1 -> 0, carry goes true
    1 + 0 -> 1, carry stays false
    0 + 0 -> 0, carry stays false

when done iterating over smaller,
case 1 -> carry is true:
    keep adding 1 to larger
    if index goes out of bounds while carrying:
        append index to [1]

case 2 -> carry is false:
    return bigger

'''
