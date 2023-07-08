from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ''
        for index, char in enumerate(strs[0]):
            for str in strs[1:]:
                if index >= len(str) or char != str[index]:
                    return output
            
            output += char
        
        return output
    