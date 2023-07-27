class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1

        lengthOfLast = 0

        while i >= 0 and s[i] != ' ':
            lengthOfLast += 1
            i -= 1

        return lengthOfLast
            
        '''
        iterate over entire string (right to left)
        skip over white space
        start counting
        when hit whitespace again or beginning of string -> return length
        
        '''
