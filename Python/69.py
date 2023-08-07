import math

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        num_digits = int(math.log10(x)) + 1

        min_values = [0]
        num_limit = 2**31 - 1
        for num in range(1, 12):
            if num % 2 != 0:
                min_values.append(10**(num // 2))
            else:
                min_values.append(math.floor((3.1622*10**(num / 2 - 1))))

        i = min_values[num_digits]

        while True:
            squared = i**2
            if squared > x:
                return i - 1
            
            i += 1

    '''
    find number of digits

    start from 1 times 10 to the power of the 
    number of digits divided by 2

    increment by 1 and square that number

    if it is greater than x, return that number - 1

    revision:
    use binary search
    
    '''
