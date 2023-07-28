from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] >= 0 and digits[i] <= 8:
                digits[i] += 1
                return digits
            
            digits[i] = 0
            i -= 1
        

        if i < 0:
            new = [1]
            for elements in digits:
                new.append(elements)
            return new
    

'''
iterate over array from right to left
    if digit is 0-8 -> increment by one, return array

    if digit is 9 -> replace 9 with 0

if i is less than 0, append array to the end of [1] -> return array

case 1:
last digit is 0-8 -> increment by one

case 2:
last digit is 9 ->
    set last digit to 0, try to increment left index by one
    go back to cases -> 
    continue until you reach the front of the array. If you need to carry still, then return the array with a 1 added on the front
'''
