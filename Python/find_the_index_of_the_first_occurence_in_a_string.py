class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            pass_test = True
            if i + len(needle) > len(haystack):
                return -1
            temp = i
            j = 0
            while j < len(needle):
                if haystack[temp] != needle[j]:
                    pass_test = False
                    break
                temp += 1
                j += 1
                
            if pass_test == True:
                return i
            
        return -1

        ''' 
        Initial code ->
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                return -1
            elif needle == haystack[i: i + len(needle)]:
                return i
            
        return -1
        '''
