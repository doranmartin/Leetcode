class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result

    '''
    find number of digits

    start from 1 times 10 to the power of the 
    number of digits divided by 2

    increment by 1 and square that number

    if it is greater than x, return that number - 1

    revision:
    use binary search
    
    '''
